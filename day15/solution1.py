import json
import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

S = set()

coords = [[int(b.strip("xy=")) for a in line.split(":") for b in a.strip(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ").split(", ")] for line in lines]

#for (x1, y1, x2, y2) in coords:
#    dist = abs(x1-x2) + abs(y1-y2)
#    print([(x1, y1, x2, y2), dist])
#    for d0 in range(dist+1):
#        d1 = dist-d0
#        for e in range(d0+1):
#            for f in range(d1+1):
#                S.add((x1-e,y1-f))
#                S.add((x1-e,y1+f))
#                S.add((x1+e,y1-f))
#                S.add((x1+e,y1+f))
#
#for (x1, y1, x2, y2) in coords:
#    try:
#        S.remove((x2,y2))
#    except: pass
#
#line_coords = [coord for coord in S if coord[1] == 10]
#print(sorted(line_coords))
#
#print(len(line_coords))

xs = set(c[0] for c in coords) | set(c[2] for c in coords)

row = 2000000

#S = set(range(min(xs), max(xs)+1))
S = set()

for (x1, y1, x2, y2) in coords:
    dist = abs(x1-x2) + abs(y1-y2)
    rowdist = abs(y1-row)
    coldist = dist - rowdist
    print([(x1, y1, x2, y2), dist, rowdist, coldist])
    if dist < rowdist:
        continue
    for v in range(x1-coldist, x1+coldist+1):
        #print(v)
        S.add(v)

for (x1, y1, x2, y2) in coords:
    if y2 == row:
        try:
            S.remove(x2)
        except: pass

#print(sorted(S))
print(len(S))
