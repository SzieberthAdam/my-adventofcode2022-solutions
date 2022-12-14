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

history = {}

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

    #print(f'ri={ri} ({rii}); j={ji} ({jii}); [{"".join(["<>"[x] for x in rockjets])}]')

    # DEAD END
    #if not rii:
    #    b = 0
    #    for i, x in enumerate(C):
    #        b |= x
    #        if b == 0x7F: break
    #    Ct = tuple(C)[:i+1]
    #    C = collections.deque(Ct)
    #    ji1 = history.setdefault(Ct, ji)
    #    if ji1 != ji:
    #        raise Exception

    if C[0] == 0x7F:
        C = collections.deque((0x7F,))
        T0, ri0 = history.setdefault((jii, rii), (T, ri))
        if ri0 != ri:
            nrocks = ri-ri0
            Td = T - T0
            fcyc, rem = divmod(N-1-ri, nrocks)
            rfw = nrocks * fcyc
            Tfw = Td * fcyc
            print(f'match found between rocks {ri0+1} and {ri+1} (count: {nrocks})')
            ri += rfw
            print(f'fast forward {nrocks} * {fcyc} = {rfw} rocks to {ri}')
            T += Tfw
            print(f'tower increased by {Td} * {fcyc} = {Tfw} to {T}')
            print("simulation continues")


            #raise Exception

        #raise Exception

    ri += 1

print(T)
