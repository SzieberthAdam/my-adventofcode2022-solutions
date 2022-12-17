import collections
import itertools
import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

jets = tuple((0 if c=="<" else 1) for c in lines[0])
del lines
J = len(jets)

if len(sys.argv) < 3:
    N = 1000000000000
else:
    N = int(sys.argv[2])

ROCKS = (
    (0x1E,),
    (0x08, 0x1C, 0x08,),
    (0x1C, 0x04, 0x04,),
    (0x10, 0x10, 0x10, 0x10),
    (0x18, 0x18),
)

R = len(ROCKS)

ROCKSo = tuple(tuple(itertools.accumulate(r, int.__ror__))[-1] for r in ROCKS)

ABOVE = 4

C = collections.deque((0xFF,))
T = 0

ji = 0
jii = 0
ri = 0
while ri < N:
    rockjets = [] ##
    rii = ri % R
    r = ROCKS[rii]
    ro = ROCKSo[rii]
    for a in range(ABOVE):
        j = jets[jii]
        rockjets.append(j) ##
        ji += 1
        jii += 1
        jii = (0 if jii==J else jii)
        if j and not (ro & 0x01):
            r = tuple(x >> 1 for x in r)
            ro = ro >> 1
        elif not j and not (ro & 0x40):
            r = tuple(x << 1 for x in r)
            ro = ro << 1
    d = 0
    #input()
    while not any((x & C[d-i]) for i, x in enumerate(r) if 0 <= d-i):
        j = jets[jii]
        rockjets.append(j) ##
        ji += 1
        jii += 1
        jii = (0 if jii==J else jii)
        if j and not (ro & 0x01):
            r1 = tuple(x >> 1 for x in r)
            ro1 = ro >> 1
            if not any((x & C[d-i]) for i, x in enumerate(r1) if 0 <= d-i):
                r = r1
                ro = ro1
        elif not j and not (ro & 0x40):
            r1 = tuple(x << 1 for x in r)
            ro1 = ro << 1
            if not any((x & C[d-i]) for i, x in enumerate(r1) if 0 <= d-i):
                r = r1
                ro = ro1
        d += 1
    rxi = 0
    for rxi in range(1, 1+min(len(r), d)):
        C[d-rxi] |= r[rxi-1]
    C.extendleft(r[rxi:])
    T += max(len(r) - d, 0)
    print(f'n={ri} ({rii}); j={ji} ({jii}); [{"".join(["<>"[x] for x in rockjets])}]')
    #print(f'{C}')
    ri += 1
    #print("".join([" ><"[x] for x in rockjets]))
    #print(f'settled: {x}; {C}; {T}; {d}')
    #input()

print(T)
