import base64
import secrets
from struct import pack
from hashlib import sha512
from binascii import unhexlify
from zlib import crc32
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


# AES256 key hardcoded in the PHP script
PROOF_AES_KEY = unhexlify("066b15fa7aede48e9591c980bf86d6791665a755477b4dd668b7b3737aaa6f27")
# PEPPER randomness hardcoded in the PHP script
# Odly enough, it is composed of hexadecimal characters, but is appended to the data as-is
# (instead of using the actual binary data represented by the hexadecimal)
PROOF_HASH_PEPPER = b'c489adbfa56334cab31a42775ff51cfb0c1752dba7d747259ff9e0f3456d33bbf47563255d8a3d89212076fc3b15f3d622ff9c3fd00e3b057792da44c51ca230'


def armor(raw: bytes) -> str:
    return base64.b64encode(raw).decode().replace("=", "@").replace("+", "-").replace("/", "_")


def generate_invalid_proof():
    # Generate 5 random pseudo sha512 hashes
    hashes = [sha512(secrets.token_bytes()).digest() for _ in range(5)]
    data = b"".join(hashes)

    # Extraction des données binaires : en-tête puis padding jusque 32 octets puis tour
    # puis 5 hashes de 64 caractères en fin de paquet (le début étant l'aléa pour CBC)
    data = b"!BB-PRF!" + secrets.token_bytes(32) + b"".join(hashes)

    # Compute CRC32
    crc = crc32(data + PROOF_HASH_PEPPER)
    data_and_crc = data + pack("<q", crc)

    # Encrypt
    iv = secrets.token_bytes(16)
    cipher = Cipher(algorithms.AES(PROOF_AES_KEY), modes.CBC(iv))
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(len(PROOF_AES_KEY) * 8).padder()
    data_with_crc_and_padding = padder.update(data_and_crc) + padder.finalize()
    ciphered = encryptor.update(data_with_crc_and_padding) + encryptor.finalize()

    return armor(iv + ciphered)


if __name__ == "__main__":
    print(generate_invalid_proof())
