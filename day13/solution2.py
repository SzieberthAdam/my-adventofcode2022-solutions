import functools
import json
import math
import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

packets = [json.loads(s) for s in lines if s]

dividerpackets = [[[2]], [[6]]]
packets.extend(dividerpackets)

def compare(p, depth=0, yield0=True):
    types = tuple(type(a) for a in p)
    if types == (list, list):
        if not p[0] and not p[1]:
            return
        if yield0:
            yield (None, 0, p, depth)
        if not p[0]:
            yield (True, 1, p, depth)
        elif not p[1]:
            yield (False, 2, p, depth)
        else:
            yield from compare((p[0][0], p[1][0]), depth+1)
            yield from compare((p[0][1:], p[1][1:]), depth, False)
    elif types == (int, list):
        yield (None, 3, p, depth+1)
        yield from compare(([p[0]], p[1]), depth+2)
    elif types == (list, int):
        yield (None, 4, p, depth+1)
        yield from compare((p[0], [p[1]]), depth+2)
    elif types == (int, int):
        if p[0] < p[1]:
            yield (True, 5, p, depth)
        elif p[0] == p[1]:
            yield (None, 6, p, depth)
        else:
            yield (False, 7, p, depth)
    else: raise NotImplementedError

def comparepackets(p1, p2):
    for cmpval, *_ in compare((p1, p2)):
        if cmpval is True: return -1
        if cmpval is False: return 1
    return 0

sortedpackets = sorted(packets, key=functools.cmp_to_key(comparepackets))

for p in sortedpackets:
    print(p)

print()

dividerlocations = [sortedpackets.index(dividerpackets[i])+1 for i in range(len(dividerpackets))]
print(dividerlocations)

print()
print(f'Answer 2: {math.prod(dividerlocations)}')
