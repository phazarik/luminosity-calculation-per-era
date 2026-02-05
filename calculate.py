#!/usr/bin/env python3

import os
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--filter", default=None)
args = parser.parse_args()

ERADIR = "eras"
NORMTAG = "/cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json"

results = []

total_sum = 0.0
for fname in sorted(os.listdir(ERADIR)):
    if not fname.endswith(".json"): continue
    if args.filter and args.filter not in fname: continue
    
    fpath = os.path.join(ERADIR, fname)
    cmd = [
        "brilcalc", "lumi",
        "-c", "web",
        "--normtag", NORMTAG,
        "-u", "/fb",
        "-i", fpath
    ]

    print("\033[1;33m")
    print(">>> ", " ".join(cmd))
    print("\033[0m")
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    output = proc.stdout
    print(output)

    totrecorded = None
    lines = output.splitlines()
    for i, line in enumerate(lines):
        if "totrecorded(/fb)" in line:
            val_line = lines[i + 2]
            fields = [f.strip() for f in val_line.strip("|").split("|")]
            totrecorded = fields[-1]
            break

    if totrecorded is not None: total_sum += float(totrecorded)
    results.append((fname.replace(".json", ""), totrecorded))

print("\033[33m\nSummary (totrecorded /fb):")
print("+----------------------+------------------+")
print("| Era                  | totrecorded(/fb) |")
print("+----------------------+------------------+")
for era, val in results:
    print(f"| {era:<20} | {val:<16} |")
print("+----------------------+------------------+\033[0m")
print(f"| {'TOTAL':<20} | {total_sum:<16.9f} |")
print("+----------------------+------------------+\033[0m")
