import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    mx = [list(_line.rstrip("\n")) for _line in _f.readlines()]

steps = [[-1 for c in row] for row in mx]

for ri, row in enumerate(mx):
    for ci, c in enumerate(row):
        if c == "S":
            S = (ri, ci)
            mx[ri][ci] = "a"
            steps[ri][ci] = 0
        elif c == "E":
            E = (ri, ci)
            mx[ri][ci] = "z"

ele = [[ord(c)-ord("a") for c in row] for row in mx]


moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
maxclimb = 1

step = 0
steplocs = set()

for ri, row in enumerate(ele):
    for ci, e in enumerate(row):
        if e == 0:
            steplocs.add((ri, ci))

while (E not in steplocs):
    step += 1
    # print(f'=== STEP {step} ===')
    newsteplocs = set()
    for ri0, ci0 in steplocs:
        ele0 = ele[ri0][ci0]
        for move in moves:
            ri1 = ri0 + move[0]
            ci1 = ci0 + move[1]
            if ri1<0: continue
            if ci1<0: continue
            try:
                ele1 = ele[ri1][ci1]
            except IndexError: continue
            else:
                if (steps[ri1][ci1] == -1) and (ele1-ele0 <= maxclimb):
                    steps[ri1][ci1] = step
                    newsteplocs.add((ri1, ci1))
    steplocs = newsteplocs

print(f'Answer 1: {step}')
