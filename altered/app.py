import os
from pathlib import Path
from hashlib import sha256
from flask import Flask, send_file, request, abort


BASE_DIR = Path(__file__).parent


app = Flask(__name__)


ITEMS = {}
for path in BASE_DIR.iterdir():
    if path.is_dir():
        ballot_box = path / "BallotBoxExport.zip"
        ballot_key = path / "BallotKeysExport.zip"
        try:
            password = (path / "password").read_text().strip()
        except FileNotFoundError:
            continue

        if not ballot_box.exists() or not ballot_key.exists():
            continue

        assert password not in ITEMS
        ITEMS[password] = (path.name, ballot_box, ballot_key)


def check_domain(name):
    if not os.environ.get("FILTER_ITEM_BY_DOMAIN"):
        return
    # verifier-mon-vote.fr use (url, authKey) as cache key, hence we serve
    # different box alterations as different subdomains
    if name not in request.url_root.lower():
        print(f"Domain/name mismatch: name={name} root_url={request.url_root}")
        abort(404)


@app.route(f"/65fae701f14479f676bf4d43cbcb2d5f9d98163afa79518b8416b7536e97ba03", methods=["POST"])
def get_box():
    try:
        name, ballot_box, _ = ITEMS[str(request.form["authKey"])]
    except KeyError:
        abort(404)

    check_domain(name)
    return send_file(ballot_box)


@app.route(f"/a341a4c3fae1a82247bdb1985f7ef2ef0dfad103917bf1ee450accf7720162f4", methods=["POST"])
def get_hash():
    try:
        name, ballot_box, _ = ITEMS[str(request.form["authKey"])]
    except KeyError:
        abort(404)

    check_domain(name)
    return sha256(ballot_box.read_bytes()).hexdigest()


@app.route(f"/474eccbbc08d2d76b8743bcb84ef15490ee1cdee75ff45fe6153a108ec12342e", methods=["POST"])
def get_keys():
    try:
        name, _, ballot_key = ITEMS[str(request.form["authKey"])]
    except KeyError:
        abort(404)

    check_domain(name)
    return send_file(ballot_key)
