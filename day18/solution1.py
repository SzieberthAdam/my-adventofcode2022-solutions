import collections
import copy
import itertools
import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

centers = set(tuple(int(x) for x in line.split(",")) for line in lines)

connected = collections.defaultdict(lambda: 0)

for cube in centers:
    x0, y0, z0 = cube
    for i in range(3):
        for d in (-1, +1):
            cube2 = list(cube)
            cube2[i] += d
            cube2 = tuple(cube2)
            if cube2 in centers:
                connected[cube] += 1

N = 6 * len(centers) - sum(connected.values())

print(N)
