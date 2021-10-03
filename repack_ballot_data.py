#! /usr/bin/env python

import argparse
from pathlib import Path
import base64
import csv
from functools import partial
import secrets
from string import ascii_lowercase
from typing import Tuple
from struct import pack
from json import loads as json_loads, dumps as json_dumps
from multiprocessing.pool import ThreadPool
from hashlib import sha512
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15


def armor(raw: bytes) -> str:
    # Armor is base64 then =+/ being replaced by @-_
    return base64.b64encode(raw).decode("ascii").replace("=", "@").replace("+", "-").replace("/", "_")


def unarmor(armored: str) -> bytes:
    # Armor is base64 then =+/ being replaced by @-_
    return base64.b64decode(armored.replace("@", "=").replace("-", "+").replace("_", "/"))


# In the CSV, each ballot is under the form
# (cipheredBallot, proofHash, integrityOk, ballotWeight)
# `integrityOk` is always 1
# `ballotWeight` is always 1 for a uninominal election
BallotRow = Tuple[str, str, int, int]


def encrypt_content(key, ballot: dict) -> bytes:
    json_part = json_dumps(ballot["json_part"])
    # Why escaping json, WHY ????
    json_part = json_part.replace("[", "(").replace("]", ")").replace("\"", "'")
    random_part = ballot.get("random_part")
    if not random_part:
        # Create random data that pad up to 373 bytes to endup with 384 bytes with PKCS1 padding
        random_part = "".join(secrets.choice(ascii_lowercase) for _ in range(373 - len(json_part)))
    cleartext = (json_part + random_part).encode("utf8")
    assert len(cleartext) <= 384
    try:
        block = key.encrypt(cleartext, padding=PKCS1v15())
    except Exception as exc:
        raise
    content = pack(">ii", 1, len(block)) + block
    return content


def build_row(key, ballot: dict) -> BallotRow:
    content_hash = ballot.get("hash")
    content = ballot.get("content")
    if not content or not content_hash:
        # Consider the ballot has been altered and must be recomputed
        content = encrypt_content(key, ballot)
        content_hash = sha512(content).digest()

        content = armor(content)
        content_hash = armor(content_hash)

    return [content, content_hash, int(ballot.get("integrity_ok", 1)), int(ballot.get("ballot_weight", 1))]


def unpack_key(key_file: Path) -> str:
    # Remove the custom armor, should leave us with the regular pem armor
    # (i.e. starting with `-----BEGIN PRIVATE KEY-----`)
    pem = unarmor(key_file.read_text())

    # Now we can actually load the key
    key = serialization.load_pem_private_key(pem, password=None).public_key()

    return key


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("json_ballot_data")
    parser.add_argument("--key-file", "-k", help="e.g. `data/keys/1M-9493O-5D-2B-1C-2T-8S.pem`")
    parser.add_argument("--output", "-o", default="ballot_data.csv")
    args = parser.parse_args()

    key = unpack_key(Path(args.key_file))
    ballots = json_loads(Path(args.json_ballot_data).read_text())
    results = []
    with ThreadPool(1) as pool:
        ret = pool.imap(partial(build_row, key), ballots)
        for i, result in enumerate(ret):
            results.append(result)
            if i % 1000 == 0:
                print(f"{i}/{len(ballots)}")

    with open(args.output, "w", encoding="utf-8-sig") as fd:
        csv_writer = csv.writer(fd, delimiter=";", quotechar="\"", quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerows(results)
