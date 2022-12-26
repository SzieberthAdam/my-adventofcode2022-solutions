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
    #print(f'NOPOS: {",".join(["("+str(int(x.real))+","+str(int(x.imag))+")" for x in sorted(nopos, key=lambda x: (x.real, x.imag))])}')
    #print(f'POS: {",".join(["("+str(int(x.real))+","+str(int(x.imag))+")" for x in sorted(pos, key=lambda x: (x.real, x.imag))])}')
    #print()

    for r in range(H):
        row = []
        for c in range(W):
            v = c+r*1j
            ch = "."
            if v in {S, E}:
                if v in pos:
                    row.append("E")
                else:
                    row.append(ch)
                continue
            if v in wallpos:
                row.append("#")
                continue
            for bt, bs in blizzards.items():
                if v in bs:
                    if ch == ".":
                        ch = bt
                    elif ch in blizzards:
                        ch = "2"
                    elif ch in "2345678":
                        ch = chr(ord(ch)+1)
            if v in pos:
                assert ch == "."
                ch = "E"
            row.append(ch)
        print("".join(row))

    print()

    if E in pos:
        break

    blizzards["<"] = {(p-1 if p-1 not in bnopos else W-2+p.imag*1j) for p in blizzards["<"]}
    blizzards[">"] = {(p+1 if p+1 not in bnopos else 1+p.imag*1j) for p in blizzards[">"]}
    blizzards["^"] = {(p-1j if p-1j not in bnopos else p.real+(H-2)*1j) for p in blizzards["^"]}
    blizzards["v"] = {(p+1j if p+1j not in bnopos else p.real+1j) for p in blizzards["v"]}

    minute += 1
