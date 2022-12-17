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

Vp = {}

Vv2 = {(v1, v2): None for v1 in Vo for v2 in Vo if v1 != v2}

while None in set(Vsh.values()):
    for (v1, v2), p in Vsh.items():
        if p is None: continue
        if v2 in Vv[v1]:
            Vsh[(v1, v2)] = (v1, v2)
        vv = {v1,}
        paths = {(v1, )}
        while True:
            newvv = set()
            for p in list(paths):
                v0 = p[-1]
                inc = False
                for v3 in Vv[v0]:
                    if v3 in vv: continue
                    if v3 in p: continue
                    p1 = p + (v3,)
                    paths.add(p1)
                    newvv.add(v3)
                    inc = True
                paths.remove(p)
            vv |= neww
            if v2 in newvv



raise Exception




paths = {("AA", )}
pathended = set()

while len(paths) != len(pathended):
    for p in list(paths):
        if p in pathended: continue
        pvv = set(p)
        rempaths = set(Vo) - pvv
        if not rempaths:
            pathended.add(p)
        print(p)
        v0 = p[-1]
        if v0 in p: pass
        inc = False
        for v1 in Vv[v0]:
            #if v1 in p: continue
            p1 = p + (v1,)
            paths.add(p1)
            inc = True
        paths.remove(p)
        #if inc:
        #    paths.remove(p)
        #else:
        #    pathended.add(p)
