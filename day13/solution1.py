import json
import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

pairs = list(zip([json.loads(s) for s in lines[0:len(lines):3]], [json.loads(s) for s in lines[1:len(lines):3]]))


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

rightpairs = []

for pn, p in enumerate(pairs, 1):
    print(f'== Pair {pn} ==')
    depth = 0
    for cmpval, reason, p1, depth in compare(p):
        if reason not in {1, 2}:
            print(f'{"  "*(depth)}- Compare {p1[0]} vs {p1[1]}')
        if reason == 1:
            print(f'{"  "*(depth+1)}- Left side ran out of items, so inputs are in the right order')
        elif reason == 2:
            print(f'{"  "*(depth+1)}- Right side ran out of items, so inputs are not in the right order')
        elif reason == 3:
            print(f'{"  "*(depth+1)}- Mixed types; convert left to {[p1[0]]} and retry comparison')
        elif reason == 4:
            print(f'{"  "*(depth+1)}- Mixed types; convert right to {[p1[1]]} and retry comparison')
        elif reason == 5:
            print(f'{"  "*(depth+1)}- Left side is smaller, so inputs are in the right order')
        elif reason == 6:
            pass
        elif reason == 7:
            print(f'{"  "*(depth+1)}- Right side is smaller, so inputs are not in the right order')
        if cmpval in (True, False): break
    if cmpval == True:
        rightpairs.append(pn)
    print()


print(rightpairs)
print(f'Answer 1: {sum(rightpairs)}')
