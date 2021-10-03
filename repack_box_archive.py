#! /usr/bin/env python

import argparse
from pathlib import Path
from zipfile import ZipFile


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ballot_box_dir")
    parser.add_argument("--password", "-p")
    parser.add_argument("--key-file", "-k", help="e.g. `data/keys/1M-9493O-5D-2B-1C-2T-8S.pem`")
    parser.add_argument("--output", "-o", default="BallotBoxExport.zip")
    args = parser.parse_args()

    with ZipFile(args.output, 'w') as z:
        z.setpassword(args.password.encode("utf8"))
        for item in Path(args.ballot_box_dir).iterdir():
            if item.is_dir():
                # No need to go deeper given the archive structure
                for subitem in item.iterdir():
                    z.write(filename=str(subitem), arcname=f"{item.name}/{subitem.name}")
            else:
                z.write(filename=str(item), arcname=item.name)
