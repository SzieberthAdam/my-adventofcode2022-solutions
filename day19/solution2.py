import collections
import copy
import itertools
import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

orcosts = []
clcosts = []
obcosts = []
for line in lines:
    linecost = line.split("costs ")
    linecost = tuple(int(s[0]) for s in linecost[1:])
    orcosts.append(linecost)
    clcost = (0,0,int(line.split(" clay. ")[0].split()[-1]),0)
    clcosts.append(clcost)
    obcost = (0, 0, 0, int(line.split()[-2]))
    obcosts.append(obcost)

bpcosts = []
for bp in range(len(lines)):
    costs = tuple((orcosts[bp][i], clcosts[bp][i], obcosts[bp][i], 0) for i in range(4))
    bpcosts.append(costs)



M = 32
Gdrop = 2
Odrop = 4

geodes = [0 for _ in range(len(lines))]

BP = 3

for bp in range(BP):
    print(f'=== Blueprint {bp+1} ===')
    costs = bpcosts[bp]
    plans = collections.defaultdict(list)
    plans[(1, 0, 0, 0)].append([0, 0, 0, 0])
    for m in range(M):
        print(f'=== Minute: {m+1} ===')
        newplans = collections.defaultdict(list)
        for R, LI in sorted(list(plans.items())):
            for I in LI:
                buyable = [0, 0, 0, 0]
                for ri, rc in enumerate(costs):
                    if all(rc[i] <= I[i] for i in range(4)):
                        buyable[ri] = 1
                for i, rn in enumerate(R):
                    I[i] += rn
                #print(f'{R} {I}')
                for ri, b in enumerate(buyable):
                    if b:
                        R1 = list(R)
                        R1[ri] += 1
                        R1 = tuple(R1)
                        I1 = list(I)
                        for i in range(4):
                            I1[i] -= costs[ri][i]
                        newplans[R1].append(I1)
                        #print(f'    {R1} {I1}')
        invs = {tuple(inv) for li in plans.values() for inv in li}
        newinvs = {tuple(inv) for li in newplans.values() for inv in li}
        g = max(inv[3] for inv in invs | newinvs)
        o = max(inv[2] for inv in invs | newinvs if inv[3] == 0)
        #print(g, o)
        for R, LI1 in list(newplans.items()):
            LI = plans[R]
            LI.extend(LI1)
            LI.sort(reverse=True)
            for a in list(LI):
                if a[3] + Gdrop <= g:
                    LI.remove(a)
                elif R[3] == 0 and a[3] == 0 and (a[2] + Odrop <= o):
                    LI.remove(a)
            if LI:
                removed = []
                for a, b in itertools.permutations(list(LI), 2):
                    if a in removed or b in removed: continue
                    if all(a[i]<=b[i] for i in range(4)):
                        removed.append(a)
                        LI.remove(a)
                plans[R] = LI
            else:
                del plans[R]
        #if g:
        #    for R in list(plans.keys()):
        #        if not R[2]:
        #            del plans[R]
        #print("done.")
        #input()
    geodes[bp] = g



print(geodes[0]*geodes[1]*geodes[2])
