import collections
import copy
import itertools
import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

centers = set(tuple(int(x) for x in line.split(",")) for line in lines)

connected = collections.defaultdict(set)
for cube in centers:
    for i in range(3):
        for d in (-1, +1):
            cube2 = list(cube)
            cube2[i] += d
            cube2 = tuple(cube2)
            if cube2 in centers:
                connected[cube].add(cube2)

N = 6 * len(centers) - sum(len(S) for S in connected.values())

print(N)


MIN = [min(cube[i] for cube in centers) for i in range(3)]
MAX = [max(cube[i] for cube in centers) for i in range(3)]

centers2 = set()
for x in range(MIN[0]+1, MAX[0]):
    for y in range(MIN[1]+1, MAX[1]):
        for z in range(MIN[2]+1, MAX[2]):
            cube2 = (x, y, z)
            if cube2 in centers: continue
            c = 0
            c += any(((x2, y, z) in centers) for x2 in range(MIN[0], x))
            c += any(((x, y2, z) in centers) for y2 in range(MIN[1], y))
            c += any(((x, y, z2) in centers) for z2 in range(MIN[2], z))
            c += any(((x2, y, z) in centers) for x2 in range(x+1, MAX[0]+1))
            c += any(((x, y2, z) in centers) for y2 in range(y+1, MAX[1]+1))
            c += any(((x, y, z2) in centers) for z2 in range(z+1, MAX[2]+1))
            if c == 6: centers2.add(cube2)

connected2 = collections.defaultdict(set)
connected3 = collections.defaultdict(set)
for cube in centers2:
    for i in range(3):
        for d in (-1, +1):
            cube2 = list(cube)
            cube2[i] += d
            cube2 = tuple(cube2)
            if cube2 in centers2:
                connected2[cube].add(cube2)
            elif cube2 in centers:
                connected3[cube].add(cube2)


N2 = 6 * len(centers2) - sum(len(S) for S in connected2.values())
print(N2)

a = sum(len(S) for S in connected3.values())
print(N-a)

print("----")

reduced = True
while reduced:
    print("w")
    reduced = False
    for cube, S2 in list(connected2.items()):
        v = len(S2)
        S3 = connected3.get(cube, set())
        v += len(S3)
        if v != 6:
            print(cube)
            for cube2 in S2:
                del connected2[cube2]
                del connected3[cube2]
                centers2.remove(cube2)
            del connected2[cube]
            del connected3[cube]
            centers2.remove(cube)
            reduced = True
            break


N3 = 6 * len(centers2) - sum(len(S) for S in connected2.values())
print(N3)

print(N-N3)

a = sum(len(S) for S in connected3.values())
print(N-a)

for z in range(MIN[2], MAX[2]+1):
    print(f'z={z}')
    print("   " + "".join(f'{(y // 10) or " "}' for y in range(MIN[1], MAX[1]+1)))
    print("   " + "".join(f'{y % 10}' for y in range(MIN[1], MAX[1]+1)))
    for y in range(MIN[1], MAX[1]+1):
        print(f'{y:>2} ' + "".join(("#" if (x, y, z) in centers else ("x" if (x, y, z) in centers2 else ".")) for x in range(MIN[0], MAX[0]+1))+f' {y:<2}')
    print("   " + "".join(f'{(y // 10) or " "}' for y in range(MIN[1], MAX[1]+1)))
    print("   " + "".join(f'{y % 10}' for y in range(MIN[1], MAX[1]+1)))
