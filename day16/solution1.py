import copy
import json
import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

Vo = {}
Vr = {}
Vv = {}
release = 0

for s in lines:
    v = s[6:8]
    Vo[v] = False
    vr = int(s.split("=")[1].split(";")[0])
    Vr[v] = vr
    vv = set([a.split()[-1] for a in s.split(", ")])
    Vv[v] = vv

plans = [[0, ["AA",], copy.deepcopy(Vo)]]
t = 0

for t in range(1, 31):
    print(f't={t}')
    for p in list(plans):
        plans.remove(p)
        r, a0, o0 = p
        r += sum(Vr[v]*o0[v] for v in Vr)
        for a in reversed(a0):
            if a != "o":
                v = a
                break
        a1 = set(Vv[v])
        if Vr[v] and not o0[v]:
            o1 = copy.deepcopy(o0)
            o1[v] = True
            p1 = [r, a0+["o"], o1]
            plans.append(p1)
        for a in a1:
            o1 = copy.deepcopy(o0)
            p1 = [r, a0+[a,], o1]
            plans.append(p1)
    plans.sort()
    plans = plans[-10000:]

r, a0, o0 = plans[-1]

print()
print(", ".join(a0))
print(r)
