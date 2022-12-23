import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

import collections
import copy
import itertools

rowrange = {}
colrange = {}

fields = set()
walls = set()

for r, line in enumerate(lines[:-2], 1):
    for c, ch in enumerate(line, 1):
        if ch==" ":
            continue
        elif ch==".":
            fields.add((r, c))
        elif ch == "#":
            fields.add((r, c))
            walls.add((r, c))

minr = min(r for r, c in fields)
maxr = max(r for r, c in fields)
minc = min(c for r, c in fields)
maxc = max(c for r, c in fields)

for r_ in range(minr, maxr+1):
    rowrange[r_] = (min(c for r, c in fields if r==r_), max(c for r, c in fields if r==r_))
for c_ in range(minc, maxc+1):
    colrange[c_] = (min(r for r, c in fields if c==c_), max(r for r, c in fields if c==c_))

cplan = lines[-1]
plan_ = ["L"+part for chunk in cplan.split("R") for part in ("R"+chunk).split("L")]
plan = []
for chunk in plan_:
    if chunk.startswith("LR"):
        chunk = chunk[1:]
    plan.append(chunk)

turnmap = {
    (3, "R"): 0,
    (0, "R"): 1,
    (1, "R"): 2,
    (2, "R"): 3,
    (1, "L"): 0,
    (2, "L"): 1,
    (3, "L"): 2,
    (0, "L"): 3,
}

r = 1
c = rowrange[r][0]
face = 3 #initial right turn

for chunk in plan:
    turn, *steps = chunk
    nsteps = int("".join(steps))
    face = turnmap[face, turn]
    for _ in range(nsteps):
        if face == 0:
            r1 = r
            c1 = c + 1
            if (r1, c1) not in fields: c1 = rowrange[r][0]
        elif face == 1:
            r1 = r + 1
            c1 = c
            if (r1, c1) not in fields: r1 = colrange[c][0]
        elif face == 2:
            r1 = r
            c1 = c - 1
            if (r1, c1) not in fields: c1 = rowrange[r][1]
        elif face == 3:
            r1 = r - 1
            c1 = c
            if (r1, c1) not in fields: r1 = colrange[c][1]
        if (r1, c1) in walls:
            break
        else:
            r, c = r1, c1

print(1000*r + 4 *c + face)
