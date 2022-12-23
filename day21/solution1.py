import pathlib
import sys

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

import collections
import copy
import itertools

N = [line.split(": ") for line in lines]
D = dict(tuple(line.split(": ")) for line in lines)
D = {n: (int(y) if y.isdecimal() else y) for n, y in D.items()}

def val(n):
    v = D[n]
    if type(v) == int:
        return v
    n1, o, n2 = v.split()
    if o == "+":
        return val(n1) + val(n2)
    elif o == "-":
        return val(n1) - val(n2)
    elif o == "*":
        return val(n1) * val(n2)
    elif o == "/":
        return val(n1) / val(n2)


print(val("root"))
