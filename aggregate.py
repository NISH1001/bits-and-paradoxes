#!/usr/bin/env python3

import os
import glob


def get_files(path):
    files = glob.glob(os.path.join(path, "*.md"))
    files = list(map(os.path.basename, files))
    files = list(filter(lambda x: x[0].isdigit(), files))
    files = sorted(files, key=lambda x: int(x[:2]))
    return files


def combine(files, delim="---\n"):
    bigchunk = ""
    contents = []
    for fname in files:
        with open(fname) as f:
            contents.append(f.read())
    return delim.join(contents)


def main():
    delim = "---\n"
    path = "."
    files = get_files(path)
    agg = combine(files, delim=delim)
    intro = "# Bits and Paradoxes\n\nAll things I loved consuming to reinforce my prior beliefs of the world around."

    final = f"{intro}\n\n{delim}\n{agg}"
    outname = "README.md"
    with open(outname, "w") as f:
        f.write(final)


if __name__ == "__main__":
    main()
