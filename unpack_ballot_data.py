#! /usr/bin/env python

import argparse
from pathlib import Path
import base64
import csv
from functools import partial
from typing import List, Tuple
from struct import unpack
from json import loads as json_loads, dumps as json_dumps
from multiprocessing.pool import ThreadPool
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15


def unarmor(armored: str) -> bytes:
    # Armor is base64 then =+/ being replaced by @-_
    return base64.b64decode(armored.replace("@", "=").replace("-", "+").replace("_", "/"))


# In the CSV, each ballot is under the form
# (cipheredBallot, proofHash, integrityOk, ballotWeight)
# `integrityOk` is always 1
# `ballotWeight` is always 1 for a uninominal election
BallotRow = Tuple[str, str, int, int]


def read_csv(ballot_data: Path) -> List[BallotRow]:
    with open(str(ballot_data), "r", encoding="utf-8-sig") as fd:
        csv_reader = csv.reader(fd, delimiter=";", quotechar="\"")
        return list(csv_reader)


def decrypt_content(key, content: str) -> dict:
    raw_content = unarmor(content)
    # Extract blocks count (most likely only one...)
    blocks_count = unpack(">i", raw_content[:4])[0]
    offset = 4
    # Extract size for each block
    blocks_sizes = []
    for i in range(blocks_count):
        blocks_sizes = [unpack(">i", raw_content[offset:offset + 4])[0]]
        offset += 4
    # Now actually decrypt each block
    cleartext = b""
    for block_size in blocks_sizes:
        block = raw_content[offset: offset + block_size]
        offset += block_size
        # Some blocks are smaller than the required padding, so must correct them
        if len(block) != 384:
            block = b"\x00" * (384 - len(block)) + block
        # PKCS1v15 not recomanded for newer applications (should use OAEP instead)
        cleartext += key.decrypt(block, padding=PKCS1v15())

    # The final result is a json (with yet another custom armor...) and some random data for hash uniqueness
    sep = cleartext.rfind(b")") + 1
    json_part = cleartext[:sep]
    random_part = cleartext[sep:]
    # Why escaping json, WHY ????
    json_part = json_part.replace(b"(", b"[").replace(b")", b"]").replace(b"'", b"\"")
    json_part = json_loads(json_part)

    return {
        "content": content,
        "blocks_sizes": blocks_sizes,
        "random_part": random_part.decode("ascii"),
        "json_part": json_part,
    }


def unpack_row(key, row: BallotRow) -> dict:
    assert len(row) == 4
    data = decrypt_content(key, row[0])
    data["hash"] = row[1]
    data["integrity_ok"] = row[2]
    data["ballot_weight"] = row[3]
    return data


def unpack_key(key_file: Path) -> str:
    # Remove the custom armor, should leave us with the regular pem armor
    # (i.e. starting with `-----BEGIN PRIVATE KEY-----`)
    pem = unarmor(key_file.read_text())

    # Now we can actually load the key
    key = serialization.load_pem_private_key(pem, password=None)

    return key


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ballot_data", help="must be `1` or `2`, or a path (e.g. `data/box/1M-9493O-5D-2B-1C-2T-8S/ballot_data.csv`)")
    parser.add_argument("--key-file", "-k", help="e.g. `data/keys/1M-9493O-5D-2B-1C-2T-8S.pem`")
    parser.add_argument("--output", "-o", default="output.json")
    args = parser.parse_args()
    if args.ballot_data == '2':
        args.ballot_data = "data/box/1M-9493O-5D-2B-1C-2T-8S/ballot_data.csv"
        args.key_file = "data/keys/1M-9493O-5D-2B-1C-2T-8S.pem"
    elif args.ballot_data == '1':
        args.ballot_data = "data/box/1M-9493O-5D-2B-1C-1T-8S/ballot_data.csv"
        args.key_file = "data/keys/1M-9493O-5D-2B-1C-1T-8S.pem"

    key = unpack_key(Path(args.key_file))
    ballots = read_csv(Path(args.ballot_data))
    results = []
    with ThreadPool() as pool:
        ret = pool.imap(partial(unpack_row, key), ballots)
        for i, result in enumerate(ret):
            results.append(result)
            if i % 1000 == 0:
                print(f"{i}/{len(ballots)}")

    Path(args.output).write_text(json_dumps(results, indent=4))
