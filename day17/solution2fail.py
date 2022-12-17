import collections
import itertools
import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

jets = tuple((-1 if c=="<" else 1) for c in lines[0])
del lines
J = len(jets)

if len(sys.argv) < 3:
    N = 1000000000000
else:
    N = int(sys.argv[2])

RB = (
    (0,0,0,0,),
    (1,0,1,),
    (0,0,0,),
    (0,),
    (0,0,)
)

RH = (
    (1,1,1,1,),
    (1,3,1,),
    (1,1,3,),
    (4,),
    (2,2,)
)

R = len(RB)

W = 7
RX = 2
ABOVE = 4

storage = {}

C = [0 for _ in range(W)]
T = max(C)

ji = 0
jii = 0
ri = 0
while ri < N:
    rii = ri % R
    rockjets = [] ##
    #print(f'rockidx: {rii}')
    rb = RB[rii]
    rh = RH[rii]
    rw = len(rb)
    x = RX
    for a in range(ABOVE):
        j = jets[jii]
        ji += 1
        jii += 1
        jii = (0 if jii==J else jii)
        x += j
        x = max(x, 0)
        x = min(x, W - rw)
        rockjets.append(j) ##
    d = 0
    while not any(rb[i]-d <= C[x+i]-T for i in range(rw)):
        j = jets[jii]
        rockjets.append(j) ##
        ji += 1
        jii += 1
        jii = (0 if jii==J else jii)

        if j == -1 and x == 0: j = 0
        elif j == 1 and W <= x + rw: j = 0
        elif any(rb[i]-d <= C[x+i+j]-T for i in range(rw)): j = 0
        x += j
        d += 1
    for i in range(rw):
        C[x+i] = T + rb[i] + rh[i] - d
    T = max(C)
    print(f'n={ri} ({rii}); j={ji} ({jii}); [{"".join([" ><"[x] for x in rockjets])}]')
    print(f'{C}')
    ri += 1
    #print("".join([" ><"[x] for x in rockjets]))
    #print(f'settled: {x}; {C}; {T}; {d}')
    #input()

print(T)
