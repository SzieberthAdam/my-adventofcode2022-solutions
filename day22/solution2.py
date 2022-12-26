import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

import collections
import copy
import itertools

rowrange = {}
colrange = {}

fields = set()
walls = set()

for r, line in enumerate(lines[:-2], 0):
    for c, ch in enumerate(line, 0):
        if ch==" ":
            continue
        elif ch==".":
            fields.add((r, c))
        elif ch == "#":
            fields.add((r, c))
            walls.add((r, c))

minr = min(r for r, c in fields)
maxr = max(r for r, c in fields)
minc = min(c for r, c in fields)
maxc = max(c for r, c in fields)

for r_ in range(minr, maxr+1):
    rowrange[r_] = (min(c for r, c in fields if r==r_), max(c for r, c in fields if r==r_))
for c_ in range(minc, maxc+1):
    colrange[c_] = (min(r for r, c in fields if c==c_), max(r for r, c in fields if c==c_))

cplan = lines[-1]
plan_ = ["L"+part for chunk in cplan.split("R") for part in ("R"+chunk).split("L")]
plan = []
for chunk in plan_:
    if chunk.startswith("LR"):
        chunk = chunk[1:]
    plan.append(chunk)

turnmap = {
    (3, "R"): 0,
    (0, "R"): 1,
    (1, "R"): 2,
    (2, "R"): 3,
    (1, "L"): 0,
    (2, "L"): 1,
    (3, "L"): 2,
    (0, "L"): 3,
}

if len(lines) < 100:  #example
    fd = {
        1: (0, 2),
        2: (1, 0),
        3: (1, 1),
        4: (1, 2),
        5: (2, 2),
        6: (2, 3),
    }

    fc = (
        ((1, 0), (6, 2), (5, 2), (3, 3), (1, 0)),
        ((1, 1), (4, 1), (5, 1), (2, 3), (1, 1)),
        ((2, 0), (3, 0), (4, 0), (6, 1), (2, 0)),
    )

    FSIZE = 4

else:
    fd = {
        1: (0, 1),
        2: (0, 2),
        3: (1, 1),
        4: (2, 0),
        5: (2, 1),
        6: (3, 0),
    }

    fc = (
        ((1, 0), (2, 0), (5, 2), (4, 2), (1, 0)),
        ((1, 1), (3, 1), (5, 1), (6, 2), (1, 1)),
        ((2, 1), (3, 2), (4, 1), (6, 1), (2, 1)),
    )

    FSIZE = 50


def getf(r, c):
    for f, t in fd.items():
        if r in range((t[0])*FSIZE-1, (1+t[0])*FSIZE) and c in range((t[1])*FSIZE-1, (1+t[1])*FSIZE):
            return f

def getcorner(f, re, ce):
    r = fd[f][0] * FSIZE + re * FSIZE - (1 if re else 0)
    c = fd[f][1] * FSIZE + ce * FSIZE - (1 if ce else 0)
    return r, c


facestep = ((0, 1), (1, 0), (0, -1), (-1, 0))

transfer = {
    (0, 0): None,#((1, 1, 0), (1, 0, 0)),
    (0, 1): ((0, 0, 0), (1, 1, 0)),
    (0, 2): ((1, 1, 0), (1, 0, 0)),
    (0, 3): ((1, 0, 0), (0, 1, 0)),
    (1, 0): ((1, 0, 1), (0, 0, 0)),
    (1, 1): ((0, 0, 0), (0, 0, 1)),
    (1, 2): ((0, 0, 1), (1, 0, 0)),
    (1, 3): ((1, 0, 0), (1, 0, 1)),
    (2, 0): ((1, 1, 0), (0, 0, 0)),
    (2, 1): ((0, 0, 0), (0, 1, 0)),
    (2, 2): None,
    (2, 3): None,
    (3, 0): ((0, 0, 1), (0, 0, 0)),
    (3, 1): ((0, 0, 0), (1, 0, 1)),
    (3, 2): None,
    (3, 3): ((1, 0, 0), (0, 0, 1)),
}

def step(r, c, face):
    r1 = r + facestep[face][0]
    c1 = c + facestep[face][1]
    face1 = face
    if (r1, c1) not in fields:
        f = getf(r, c)
        key = (f, face)
        #print("not in: ", (r, c), (r1, c1), key)
        #print((r, c, face), (r1, c1, face1))
        for i in range(3):
            fc1 = fc[i]
            try: j = fc1.index(key)
            except: continue
            key1 = fc1[j+1]
            break
        else:
            for i in range(3):
                fc1 = tuple((t[0], (t[1] + 2) % 4) for t in reversed(fc[i]))
                #print(i, fc1, key)
                try: j = fc1.index(key)
                except: continue
                key1 = fc1[j+1]
                break
            else:
                #print(key, r, c)
                raise Exception
        f1, face1 = key1
        trr, trc = transfer[(face, face1)]
        rbe, rrm, rcm = trr
        cbe, crm, ccm = trc
        r0, c0 = getcorner(f, 0, 0)
        r1, c1 =  getcorner(f1, rbe, cbe)
        rbem = -1 if rbe else 1
        r1 += rbem * ( rrm * (r-r0) + rcm * (c-c0))
        cbem = -1 if cbe else 1
        c1 += cbem * ( crm * (r-r0) + ccm * (c-c0))
        #print(f, key, fc1, j, key1, transfer[(face, face1)], getcorner(f1, rbe, cbe), r1, c1, rbem, cbem)
        print(f'OVER EDGE [{r1+1}, {c1+1}, {face1}]')
    return r1, c1, face1

fturn = {
    (1,2): (4,0),
    (1,3): (6,0),
    (2,0): (5,2),
    (2,1): (3,2),
    (2,3): (6,3),
    (3,0): (2,3),
    (3,2): (4,1),
    (5,0): (2,2),
    (5,1): (6,2),
    (4,2): (1,0),
    (4,3): (3,0),
    (6,0): (5,3),
    (6,1): (2,1),
    (6,2): (1,1),
}

r = 0
c = rowrange[r][0]
face = 3 #initial right turn

for chunk in plan:
    print(f'CHUNK: {chunk}')
    turn, *steps = chunk
    nsteps = int("".join(steps))
    face = turnmap[face, turn]
    for stepi in range(nsteps):
        r1, c1, face1 = step(r, c, face)
        if (r1, c1) in walls:
            print(f'[{r+1}, {c+1}, {face}] & WALL')
            break
        else:
            r, c = r1, c1
            face = face1
    else:
        print(f'[{r+1}, {c+1}, {face}]')

print(1000*(r+1) + 4 *(c+1) + face)
