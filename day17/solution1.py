import itertools
import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

jets_ = lines[0]

rocks = [
    (0, 1, 2, 3),
    (1,0-1j,1-1j,2-1j,1-2j),
    (0,1,2,2-1j,2-2j),
    (0,0-1j,0-2j,0-3j),
    (0,1,0-1j,1-1j),
]

W = 7
x0 = 3
y0 = 0-4j

N = 2022

C = set()

Y = 0

jets = itertools.cycle(jets_)
rocks = enumerate(itertools.cycle(rocks), 1)

rock = None
for j in jets:
    if rock is None:
        n, rock = next(rocks)
        #print(n)
        if n == N+1:
            print()
            print(Y)
            exit(0)
        c1 = x0+y0+(Y*-1j)
        #print("n:", {c+c1 for c in rock})
    #print(j)
    if j == "<": c2 = c1-1
    else: c2 = c1+1
    for c in rock:
        c3 = c+c2
        if (0 < c3.real) and (c3.real <= W) and (c3 not in C): continue
        c2=c1
        break
    c2 = c2+1j
    for c in rock:
        c3 = c+c2
        if (c3.imag <= -1) and (c3 not in C): continue
        break
    else: #no rest
        c1 = c2
        C1 = {c+c2 for c in rock}
        #print("no rest:", C1)
        continue
    c2 = c2-1j
    C1 = {c+c2 for c in rock}
    y1 = min(c.imag for c in C1)
    Y = max(Y, int(-y1))
    print(f'rock {n} rest: {C1}; tower: {Y}')
    #print(Y)
    #input()
    C |= C1
    rock = None
