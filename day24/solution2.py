import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

import collections
import copy
import itertools


moves = (1, -1, 1j, -1j)

H = len(lines)
W = len(lines[0])

S = 1
E = W-2 + (H-1)*1j

wallpos = {S-1-1j,S-1j,S+1-1j,E-1+1j,E+1j,E+1+1j}

blizzards = {
    "<": set(),
    ">": set(),
    "^": set(),
    "v": set(),
}

for r, row in enumerate(lines):
    for c, v in enumerate(row):
        if v == "#":
            wallpos.add(c+r*1j)
        elif v in blizzards:
            blizzards[v].add(c+r*1j)

bnopos = wallpos | {S, E}

pos = {S}

minute = 0
while True:
    nopos = set(p for bs in blizzards.values() for p in bs)
    pos = (pos | set(p0+m for p0, m in itertools.product(pos, moves))) - nopos - wallpos

    print(f'Minute: {minute}; Set size: {len(pos)}')

    blizzards["<"] = {(p-1 if p-1 not in bnopos else W-2+p.imag*1j) for p in blizzards["<"]}
    blizzards[">"] = {(p+1 if p+1 not in bnopos else 1+p.imag*1j) for p in blizzards[">"]}
    blizzards["^"] = {(p-1j if p-1j not in bnopos else p.real+(H-2)*1j) for p in blizzards["^"]}
    blizzards["v"] = {(p+1j if p+1j not in bnopos else p.real+1j) for p in blizzards["v"]}

    minute += 1

    if E in pos:
        print(" === FIRST TRIP ENDS ===")
        break

pos = {E}

while True:
    nopos = set(p for bs in blizzards.values() for p in bs)
    pos = (pos | set(p0+m for p0, m in itertools.product(pos, moves))) - nopos - wallpos

    print(f'Minute: {minute}; Set size: {len(pos)}')

    blizzards["<"] = {(p-1 if p-1 not in bnopos else W-2+p.imag*1j) for p in blizzards["<"]}
    blizzards[">"] = {(p+1 if p+1 not in bnopos else 1+p.imag*1j) for p in blizzards[">"]}
    blizzards["^"] = {(p-1j if p-1j not in bnopos else p.real+(H-2)*1j) for p in blizzards["^"]}
    blizzards["v"] = {(p+1j if p+1j not in bnopos else p.real+1j) for p in blizzards["v"]}

    minute += 1

    if S in pos:
        print(" === SECOND TRIP ENDS ===")
        break

pos = {S}

while True:
    nopos = set(p for bs in blizzards.values() for p in bs)
    pos = (pos | set(p0+m for p0, m in itertools.product(pos, moves))) - nopos - wallpos

    print(f'Minute: {minute}; Set size: {len(pos)}')

    if E in pos:
        print(" === THIRD TRIP ENDS: DONE ===")
        break

    blizzards["<"] = {(p-1 if p-1 not in bnopos else W-2+p.imag*1j) for p in blizzards["<"]}
    blizzards[">"] = {(p+1 if p+1 not in bnopos else 1+p.imag*1j) for p in blizzards[">"]}
    blizzards["^"] = {(p-1j if p-1j not in bnopos else p.real+(H-2)*1j) for p in blizzards["^"]}
    blizzards["v"] = {(p+1j if p+1j not in bnopos else p.real+1j) for p in blizzards["v"]}

    minute += 1
