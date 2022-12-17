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

plans = [[0, [["AA"],["AA"]], copy.deepcopy(Vo)]]
t = 0

T = 26

for t in range(1, T+1):
    print(f't={t}')
    for p in list(plans):
        plans.remove(p)
        r, (a01, a02), o0 = p
        r += sum(Vr[v]*o0[v] for v in Vr)
        for ai1, v1 in enumerate(reversed(a01)):
            if v1 != "op":
                break
        a11 = set(Vv[v1])
        if Vr[v1] and not o0[v1]:
            a11.add("op")
        for ai2, v2 in enumerate(reversed(a02)):
            if v2 != "op":
                break
        a12 = set(Vv[v2])
        if Vr[v2] and not o0[v2]:
            a12.add("op")
        for a1 in a11:
            #if a1 != "op":
            #    pa1 = next(i for i in reversed(range(len(li))) if li[i] == 'a')
            for a2 in a12:
                if v1 == v2 and a1=="op" and a2=="op":
                    continue

                o1 = copy.deepcopy(o0)
                if a1 == "op":
                    o1[v1] = True
                if a2 == "op":
                    o1[v2] = True
                p1 = [r, [a01+[a1], a02+[a2]], o1]
                plans.append(p1)
    plans.sort()
    plans = plans[-30000:]

    print("P1: " + ",".join(a01))
    print("P2: " + ",".join(a02))
    print(r)
    print()

r, (a01, a02), o0 = plans[-1]

print()
print("P1: " + ", ".join(a01))
print("P2: " + ", ".join(a02))
print(r)
