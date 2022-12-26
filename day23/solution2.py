import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

import collections
import copy
import itertools

elves = set()

alldir = (-1-1j, -1, -1+1j, 0+1j, 1+1j, 1, 1-1j, 0-1j)

dirchecks = (
    (-1, -1-1j, -1+1j),
    (1, 1-1j, 1+1j),
    (0-1j, -1-1j, 1-1j),
    (0+1j, -1+1j, 1+1j)
)

dirgen = itertools.cycle([0, 1, 2, 3])


for r, row in enumerate(lines):
    for c, v in enumerate(row):
        if v == "#":
            elves.add(r+c*1j)

roundnr = 0
while True:
    roundnr += 1
    print(f'=== ROUND {roundnr} ===')
    moves = 0
    elves_next = {}
    fields_next = collections.defaultdict(set)
    di0 = next(dirgen)
    for elf in elves:
        if any(elf+d in elves for d in alldir):
            for di1 in range(di0, di0+4):
                di2 = di1 % 4
                di = dirchecks[di2]
                if not any(elf+d in elves for d in di):
                    elves_next[elf] = elf+di[0]
                    fields_next[elf+di[0]].add(elf)
                    moves += 1
                    break
            else:
                elves_next[elf] = elf
                fields_next[elf].add(elf)
        else:
            elves_next[elf] = elf
            fields_next[elf].add(elf)
    for elf0, elf1 in elves_next.items():
        if elf0 != elf1 and len(fields_next[elf1]) == 1:
            elves.remove(elf0)
            elves.add(elf1)
    #boxreal = [
    #    min(int(elf.real) for elf in elves),
    #    max(int(elf.real) for elf in elves),
    #]
    #boximag = [
    #    min(int(elf.imag) for elf in elves),
    #    max(int(elf.imag) for elf in elves),
    #]
    #for r in range(boxreal[0], boxreal[1]+1):
    #    print("".join(("#" if r+c*1j in elves else ".") for c in range(boximag[0], boximag[1]+1)))
    if moves == 0:
        break

#boxwidth = boximag[1] - boximag[0] + 1
#boxheight = boxreal[1] - boxreal[0] + 1
#print(boxwidth * boxheight - len(elves))
