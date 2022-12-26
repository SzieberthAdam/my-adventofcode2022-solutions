import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

import collections
import copy
import itertools

def todec(s):
    v = 0
    for i, c in enumerate(reversed(s)):
        if c=="=":
            v += -2 * 5**i
        elif c=="-":
            v += -1 * 5**i
        elif c=="1":
            v += 1 * 5**i
        elif c=="2":
            v += 2 * 5**i
    return v

def tosna(v):
    s = ""
    i = 1
    while v:
        #print([s, i , v])
        d, m0 = divmod(v, 5**i)
        m = m0 // 5**(i-1)
        if m in {0,1,2}:
            s = str(m)+s
            v = d*5**i
        elif m == 3:
            s = "="+s
            v = (d+1)*5**i
        elif m == 4:
            s = "-"+s
            v = (d+1)*5**i
        else:
            raise Exception
        #print([s, i , v, d, m])
        #print()
        i+=1
    return s

total = sum(todec(v) for v in lines)
print(total)
print(tosna(total))
