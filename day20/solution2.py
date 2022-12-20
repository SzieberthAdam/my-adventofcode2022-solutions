import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

import collections
import copy
import itertools

K = 811589153

#D = collections.deque()
D = collections.defaultdict(lambda: 0)
L = []
for x in lines:
    D[int(x)*K] +=1
    imag = D[int(x)*K]
    v = int(x)*K + imag*1j
    L.append(v)

O = L[:]

#raise Exception

for r in range(10):
    print(r)
    protect = [False for i in range(len(L))]
    for o in range(len(O)):
        v = O[o]
        i = L.index(v)
        pprotect = protect[:]
        pL = L[:]
        #print()
        #print(L)
        i2 = (i + int(v.real)) % (len(L)-1)
        #print(i, v, i2)
        #input()
        del L[i]
        L.insert(i2, v)
        i3, i4 = sorted([i, i2])

        if [i3, i4] == [i, i2]:
            protect = protect[:i3] + protect[i3+1:i4+1] + [True] + protect[i4+1:]
        else:
            protect = protect[:i3] + [True] + protect[i3:i4] + protect[i4+1:]

        #print(L)
        #print(protect)
        #print(protect)
        assert protect.count(True) == o+1
        #input()

print("done.")

#print(protect)
#print(L)

gen = itertools.cycle(L)
vv = []
v = 0
for x in gen:
    if x.real == 0: break

for i in range(1, 3001):
    x = next(gen).real
    if i % 1000 == 0:
        vv.append(x)

v = sum(vv)
print(vv)
print(int(v.real))
