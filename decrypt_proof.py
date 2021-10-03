import argparse
import base64
from binascii import unhexlify
from struct import unpack
from zlib import crc32
from typing import List
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


# AES256 key hardcoded in the PHP script
PROOF_AES_KEY = unhexlify("066b15fa7aede48e9591c980bf86d6791665a755477b4dd668b7b3737aaa6f27")
# PEPPER randomness hardcoded in the PHP script
# Odly enough, it is composed of hexadecimal characters, but is appended to the data as-is
# (instead of using the actual binary data represented by the hexadecimal)
PROOF_HASH_PEPPER = b'c489adbfa56334cab31a42775ff51cfb0c1752dba7d747259ff9e0f3456d33bbf47563255d8a3d89212076fc3b15f3d622ff9c3fd00e3b057792da44c51ca230'

text = base64.b64decode("IUJCLVBSRiGv70bVqWFA+EZYPwU4p7Xkf6jq/LfsyxoBAAAAAQAAAJHUlcT0x4fRaTdjV2HH0XWL50ja7yXO5OXs6mAlVKSi9uvuMKWbNU/8mr0klEG90c6NlNyQ1NlrRTORz5bWYOdhWCVNnhvvg+pu9tsJKwe2ZymM4xS9PkC4r0qcp3l/ybHL6F30h50DHL52zwSLHG2E8m+DihdQ2tgCrP3pgs4O5KMP/hlJLXWDtFD6Aje7gT2P7ednGHenfHczTbMaxYxFt5TdNvXaJCwEGcJg2W49srLADiMkdERZDHWuxB4OsSA5c4YVldu4JV+xokH0DKICXowoifgqP1sOiqOyWMtZwyIDd7j5q68opINghFf/hXtqy8iNysFDekXngmwSRTsD+JvAig4awSp9ZVW3MVzqzQZbeuBIB9ZqD47htWBmIJQPYBHsrAHIP3t7igTqGKLf5L+cCKJMmcW1GjzXnzbA")
pepper = base64.b64decode("YzQ4OWFkYmZhNTYzMzRjYWIzMWE0Mjc3NWZmNTFjZmIwYzE3NTJkYmE3ZDc0NzI1OWZmOWUwZjM0NTZkMzNiYmY0NzU2MzI1NWQ4YTNkODkyMTIwNzZmYzNiMTVmM2Q2MjJmZjljM2ZkMDBlM2IwNTc3OTJkYTQ0YzUxY2EyMzA=")
both = base64.b64decode("IUJCLVBSRiGv70bVqWFA+EZYPwU4p7Xkf6jq/LfsyxoBAAAAAQAAAJHUlcT0x4fRaTdjV2HH0XWL50ja7yXO5OXs6mAlVKSi9uvuMKWbNU/8mr0klEG90c6NlNyQ1NlrRTORz5bWYOdhWCVNnhvvg+pu9tsJKwe2ZymM4xS9PkC4r0qcp3l/ybHL6F30h50DHL52zwSLHG2E8m+DihdQ2tgCrP3pgs4O5KMP/hlJLXWDtFD6Aje7gT2P7ednGHenfHczTbMaxYxFt5TdNvXaJCwEGcJg2W49srLADiMkdERZDHWuxB4OsSA5c4YVldu4JV+xokH0DKICXowoifgqP1sOiqOyWMtZwyIDd7j5q68opINghFf/hXtqy8iNysFDekXngmwSRTsD+JvAig4awSp9ZVW3MVzqzQZbeuBIB9ZqD47htWBmIJQPYBHsrAHIP3t7igTqGKLf5L+cCKJMmcW1GjzXnzbAYzQ4OWFkYmZhNTYzMzRjYWIzMWE0Mjc3NWZmNTFjZmIwYzE3NTJkYmE3ZDc0NzI1OWZmOWUwZjM0NTZkMzNiYmY0NzU2MzI1NWQ4YTNkODkyMTIwNzZmYzNiMTVmM2Q2MjJmZjljM2ZkMDBlM2IwNTc3OTJkYTQ0YzUxY2EyMzA=")
crc = 3959982897


def armor(raw: bytes) -> str:
    return base64.b64encode(raw).decode().replace("=", "@").replace("+", "-").replace("/", "_")


def unarmor(armored: str) -> bytes:
    return base64.b64decode(armored.replace("@", "=").replace("-", "+").replace("_", "/"))


def get_hashes_from_proof(proof: str) -> List[bytes]:
    raw = unarmor(proof)

    iv = raw[:16]
    ciphered = raw[16:]

    cipher = Cipher(algorithms.AES(PROOF_AES_KEY), modes.CBC(iv))
    decryptor = cipher.decryptor()
    data_with_crc_and_padding = decryptor.update(ciphered) + decryptor.finalize()
    unpadder = padding.PKCS7(len(PROOF_AES_KEY) * 8).unpadder()
    data_with_crc = unpadder.update(data_with_crc_and_padding) + unpadder.finalize()

    data = data_with_crc[:-8]
    crc = unpack("<q", data_with_crc[-8:])[0]
    computed_crc = crc32(data + PROOF_HASH_PEPPER)
    if crc != computed_crc:
        print(f"BAD CRC: expected {crc}, got {computed_crc}")

    expected_header = b"!BB-PRF!"
    header = data[:len(expected_header)]
    if header != expected_header:
        print(f"BAD headre: expected {expected_header:!r}, got {header!r}")

    # Extraction des données binaires : en-tête puis padding jusque 32 octets puis tour
    # puis 5 hashes de 64 caractères en fin de paquet (le début étant l'aléa pour CBC)
    hashes = data[40:]
    assert len(hashes) == 5 * 64
    hashes = [hashes[(i * 64): ((i + 1) * 64)] for i in range(5)]
    return hashes


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("proof_of_vote")
    args = parser.parse_args()
    hashes = get_hashes_from_proof(args.proof_of_vote)
    print("Your proof contains the following hashes:")
    for hash in hashes:
        # re-armor the hash to be able to grep it in ballot_data.csv
        print(armor(hash))
