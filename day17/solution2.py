import collections
import itertools
import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

jets_ = lines[0]

rocks_ = [
    (0, 1, 2, 3),
    (1,0-1j,1-1j,2-1j,1-2j),
    (0,1,2,2-1j,2-2j),
    (0,0-1j,0-2j,0-3j),
    (0,1,0-1j,1-1j),
]

W = 7
x0 = 3
y0 = 0-4j

if len(sys.argv) < 3:
    N = 1000000000000
else:
    N = int(sys.argv[2])

Cx = [[0 for _ in range(W)] for _2 in range(10)]

raise Exception

Cx = (None,) + tuple(collections.deque() for _ in range(W))
Cxk = 5

Y = 0

jets = itertools.cycle(jets_)
rocks = enumerate(itertools.cycle(rocks_), 1)

rock = None
for j in jets:
    if rock is None:
        n, rock = next(rocks)
        if (n % 1000000) == 0:
            print(n)
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
        c3r = int(c3.real)
        if (0 < c3r) and (c3r <= W) and (c3.imag not in Cx[c3r]): continue
        c2=c1
        break
    c2 = c2+1j
    for c in rock:
        c3 = c+c2
        c3r = int(c3.real)
        if (c3.imag <= -1) and (c3.imag not in Cx[c3r]): continue
        break
    else: #no rest
        c1 = c2
        #print(f'no rest: {c+c2 for c in rock}')
        continue
    c2 = c2-1j
    C1 = {c+c2 for c in rock}
    y1 = min(c.imag for c in C1)
    Y = max(Y, int(-y1))
    for c in C1:
        cr = int(c.real)
        Cx[cr].append(c.imag)
        if Cxk < len(Cx[cr]):
            Cx[cr].popleft()
    rock = None
