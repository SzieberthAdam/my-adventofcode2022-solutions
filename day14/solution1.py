import json
import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

rockpaths = [[[int(x) for x in coord.split(",")] for coord in line.split(" -> ")] for line in lines]

coords = [coord for path in rockpaths for coord in path] + [[500, 0]]

xmin = min(c[0] for c in coords) - 1
xmax = max(c[0] for c in coords)
ymin = min(c[1] for c in coords)
ymax = max(c[1] for c in coords) + 3
width = xmax - xmin + 1
height = ymax - ymin + 1

m = [["." for _ in range(width)] for _ in range(height)]

for path in rockpaths:
    for pi in range(len(path) - 1):
        p1, p2 = path[pi], path[pi+1]
        xs = set([p1[0], p2[0]])
        ys = set([p1[1], p2[1]])
        xrange = range(min(xs), max(xs)+1)
        yrange = range(min(ys), max(ys)+1)
        for x0 in xrange:
            x1 = x0 - xmin
            for y0 in yrange:
                y1 = y0 - ymin
                m[y1][x1] = "#"

print("\n".join("".join(line) for line in m))

print()
print("=== SAND SIMULATION ===")
print()

done = False
sandnr = 0
while not done:
    sandnr += 1
    settled = False
    sax0, say0 = 500, 0
    while not settled:
        movetargets = [[sax0, say0+1], [sax0-1, say0+1], [sax0+1, say0+1]]
        for sax1, say1 in movetargets:
            if say1 == ymax:
                done = True
                break
            x2 = sax1-xmin
            y2 = say1-ymin
            if m[y2][x2] == ".":
                sax0, say0 = sax1, say1
                break
        else:
            settled = True
            break
        if done:
            break
    if done:
        sandnr -=1
        break
    else:
        m[say0-ymin][sax0-xmin] = "o"

print("\n".join("".join(line) for line in m))

print(f'Answer 1: {sandnr}')
