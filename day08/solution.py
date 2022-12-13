example = """30373
25512
65332
33549
35390"""

elines = example.split("\n")

ilines = []
import pathlib
with pathlib.Path("input.txt").open() as _f:
    ilines = [_line.rstrip("\n") for _line in _f.readlines()]


def vis(mx, ri, ci):
    r = set()
    v = mx[ri][ci]
    if ri == 0 or all(mx[ri2][ci]<v for ri2 in range(0, ri)):
        r.add("top")
    if ri == (len(mx) - 1) or all(mx[ri2][ci]<v for ri2 in range(ri+1, len(mx))):
        r.add("bottom")
    if ci == 0 or all(mx[ri][ci2]<v for ci2 in range(0, ci)):
        r.add("left")
    if ci == (len(mx[ri]) - 1) or all(mx[ri][ci2]<v for ci2 in range(ci+1, len(mx[ri]))):
        r.add("right")
    return r

mx = elines
viscount = 0
for ri, col in enumerate(mx):
    for ci, v in enumerate(col):
        vi = vis(mx, ri, ci)
        print(f'({ri}, {ci}): {v} -> {vi}')
        if vi:
            viscount += 1

print(f'Answer 1 (example): {viscount}')


mx = ilines
viscount = 0
for ri, col in enumerate(mx):
    for ci, v in enumerate(col):
        vi = vis(mx, ri, ci)
        if vi:
            viscount += 1

print(f'Answer 1: {viscount}')


def vdists(mx, ri, ci):
    v = mx[ri][ci]
    dists = [0, 0, 0, 0]
    for ri2 in range(ri-1, -1, -1):
        dists[0] += 1
        if mx[ri2][ci] >= v:
            break
    for ci2 in range(ci-1, -1, -1):
        dists[1] += 1
        if mx[ri][ci2] >= v:
            break
    for ri2 in range(ri+1, len(mx)):
        dists[2] += 1
        if mx[ri2][ci] >= v:
            break
    for ci2 in range(ci+1, len(mx[ri])):
        dists[3] += 1
        if mx[ri][ci2] >= v:
            break
    return dists

def scenicscore(mx, ri, ci):
    import math
    return math.prod(vdists(mx, ri, ci))


mx = elines
for ri, col in enumerate(mx):
    for ci, v in enumerate(col):
        print(f'({ri}, {ci}): {v} -> {vdists(mx, ri, ci)} -> {scenicscore(mx, ri, ci)}')

mx = ilines

hiscore = 0
for ri, col in enumerate(mx):
    for ci, v in enumerate(col):
        hiscore = max(hiscore, scenicscore(mx, ri, ci))

print(f'Answer 2: {hiscore}')
