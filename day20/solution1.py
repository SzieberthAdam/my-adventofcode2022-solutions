import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

import collections
import copy
import itertools


#D = collections.deque()
L = [int(x) for x in lines]

protect = [False for i in range(len(L))]

for a in range(len(L)):
    pL = L[:]
    pprotect = protect[:]
    i = protect.index(False)
    v = L[i]
    #print()
    #print(L)
    i2 = (i + v) % (len(L)-1)
    #print(i, v, i2)
    #input()
    del L[i]
    L.insert(i2, v)
    i3, i4 = sorted([i, i2])

    if [i3, i4] == [i, i2]:
        protect = pprotect[:i3] + pprotect[i3+1:i4+1] + [True] + pprotect[i4+1:]
    else:
        protect = pprotect[:i3] + [True] + pprotect[i3:i4] + pprotect[i4+1:]

    #print(L)
    #print(pprotect)
    #print(protect)
    assert protect.count(True) == a+1
    #input()

print("done.")

#print(protect)
#print(L)

gen = itertools.cycle(L)
vv = []
v = 0
for x in gen:
    if x == 0: break

for i in range(1, 3001):
    x = next(gen)
    if i % 1000 == 0:
        vv.append(x)

v = sum(vv)
print(vv)
print(v)
