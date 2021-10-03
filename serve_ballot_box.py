import argparse
from pathlib import Path
from hashlib import sha256
from flask import Flask, send_file


BALLOT_BOX_PATH = None
BALLOT_KEYS_PATH = None


app = Flask(__name__)


@app.route("/65fae701f14479f676bf4d43cbcb2d5f9d98163afa79518b8416b7536e97ba03", methods=["POST"])
def get_box():
    return send_file(BALLOT_BOX_PATH)


@app.route("/a341a4c3fae1a82247bdb1985f7ef2ef0dfad103917bf1ee450accf7720162f4", methods=["POST"])
def get_box_hash():
    return sha256(BALLOT_BOX_PATH.read_bytes()).hexdigest()


@app.route("/474eccbbc08d2d76b8743bcb84ef15490ee1cdee75ff45fe6153a108ec12342e", methods=["POST"])
def get_keys():
    return send_file(BALLOT_KEYS_PATH)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ballot-box")
    parser.add_argument("--ballot-keys")
    args = parser.parse_args()

    BALLOT_BOX_PATH = Path(args.ballot_box)
    BALLOT_KEYS_PATH = Path(args.ballot_keys)

    app.run()
