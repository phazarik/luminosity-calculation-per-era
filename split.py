#!/usr/bin/env python3

import json
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--json", required=True, help="Path to golden JSON (e.g. goldenJSONs/Legacy_2016.json)")
parser.add_argument("--run", required=True, help="Path to runs JSON (e.g. runs/2016.json)")
args = parser.parse_args()

print("Reading golden JSON:", args.json)
with open(args.json) as f: golden = json.load(f)
print("Reading runs JSON:", args.run)
with open(args.run) as f: runs = json.load(f)

os.makedirs("eras", exist_ok=True)
print("Output directory: eras/")

golden_int = {}
for k, v in golden.items(): golden_int[int(k)] = v

print("Total runs in golden JSON:", len(golden_int))

for era, runlist in runs.items():
    out = {}
    for r in runlist:
        if r in golden_int:
            out[str(r)] = golden_int[r]

    if len(out) == 0:
        print("Era", era, ": no matching runs, skipped")
        continue

    outname = "eras/" + era + ".json"
    with open(outname, "w") as f: json.dump(out, f, indent=2, sort_keys=True)

    print("Era", era, ": wrote", len(out), "runs to", outname)
