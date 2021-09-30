import os
import sys
import argparse
from pathlib import Path
from typing import Dict

parser = argparse.ArgumentParser(
    description="Consolidate directories with common prefixes")
parser.add_argument("root", type=Path,
                    help="Path to the root directory to perform work in")
parser.add_argument("--delimiter", default="-",
                    help="delimiter to  use for matching prefixes")
parser.add_argument("--include-files", "-f", action="store_true")
parser.add_argument("--case-insensitive", "-i", action="store_true",
                    help="Whether or not to ignore case in prefix matching. Note: This will make the final directory names lowercase")
parser.add_argument("--dry-run", "-d", action="store_true",
                    help="Print plans instead of making changes")


def strip_prefix(filename):
    return filename.split(args.delimiter)[0].strip()


if __name__ == "__main__":
    args = parser.parse_args(sys.argv[1:])
    root = args.root
    if not root.exists():
        raise FileNotFoundError("Root directory does not exist")

    paths_with_delimiter = root.glob(f"*{args.delimiter}*")
    if not args.include_files:
        paths_with_delimiter = filter(
            lambda p: p.is_dir(), paths_with_delimiter)

    def get_prefix(name): return \
        strip_prefix(name).lower() if args.case_insensitive \
        else strip_prefix(name)

    prefixes = dict()
    for path in paths_with_delimiter:
        prefix = get_prefix(path.name)
        if prefix in prefixes:
            prefixes[prefix].append(path)
        else:
            prefixes[prefix] = [path]

    for prefix in prefixes.keys():
        aggregate_dir = root.joinpath(prefix)
        if args.dry_run:
            print(aggregate_dir)
        elif not aggregate_dir.exists():
            aggregate_dir.mkdir()
        for path in prefixes[prefix]:
            short_name = args.delimiter.join(
                path.name.split(args.delimiter)[1:]).strip()
            new_path = aggregate_dir.joinpath(short_name)
            if not args.dry_run:
                path.rename(new_path)
            else:
                print(f"-- {short_name}")
