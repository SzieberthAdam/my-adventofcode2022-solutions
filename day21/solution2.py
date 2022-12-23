import pathlib
import sys

from fractions import Fraction

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

import collections
import copy
import itertools

N = [line.split(": ") for line in lines]
D = dict(tuple(line.split(": ")) for line in lines)
D = {n: (Fraction(y) if y.isdecimal() else y) for n, y in D.items()}

class Op:
    def __init__(self, v1, o, v2):
        self.v1 = v1
        self.v2 = v2
        self.o = o

    def __call__(self):
        v1 = self.v1
        v2 = self.v2
        if type(v1)==Fraction and type(v2)==Fraction:
            if o == "+": return Fraction(v1+v2)
            if o == "-": return Fraction(v1-v2)
            if o == "*": return Fraction(v1*v2)
            if o == "/": return Fraction(v1/v2)
        v1 = self.v1 if type(self.v1) in (Fraction, str) else self.v1()
        v2 = self.v2 if type(self.v2) in (Fraction, str) else self.v2()
        if type(v1)==Fraction and type(v2)==Fraction:
            if o == "+": return Fraction(v1+v2)
            if o == "-": return Fraction(v1-v2)
            if o == "*": return Fraction(v1*v2)
            if o == "/": return Fraction(v1/v2)
        if self.o == "==":
            #print(self)
            v = None
            op = None
            if type(v1)==Fraction and type(v2)==Op:
                v = v1
                op = v2
            elif type(v2)==Fraction and type(v1)==Op:
                v = v2
                op = v1
            if v:
                op2 = None
                if type(op.v1)==Fraction:
                    if op.o == "+": op2 = Op(Fraction(v-op.v1), self.o, op.v2)
                    if op.o == "-":
                        print("ITT1")
                        op2 = Op(Fraction(op.v1-v), self.o, op.v2)
                    if op.o == "*": op2 = Op(Fraction(v/op.v1), self.o, op.v2)
                    if op.o == "/":
                        print("ITT")
                        op2 = Op(Fraction(op.v1/v), self.o, op.v2)
                elif type(op.v2)==Fraction:
                    if op.o == "+": op2 = Op(Fraction(v-op.v2), self.o, op.v1)
                    if op.o == "-": op2 = Op(Fraction(v+op.v2), self.o, op.v1)
                    if op.o == "*": op2 = Op(Fraction(v/op.v2), self.o, op.v1)
                    if op.o == "/": op2 = Op(Fraction(v*op.v2), self.o, op.v1)
                if op2:
                    #print(op2)
                    #print()
                    return op2()
        return self

    def __str__(self):
        return f'({self.v1} {self.o} {self.v2})'


def val(n):
    if n == "humn":
        return "H"
        return Fraction("20289789945740637/2501")
    v = D[n]
    if type(v) == Fraction:
        return v
    n1, o, n2 = v.split()
    v1 = val(n1)
    v2 = val(n2)
    if n == "root":
        if type(v1)==Fraction and type(v2)==Fraction:
            print(v1, v2)
            return v1==v2
        o = "=="
        #return f'({v1} == {v2})'
    if o == "+":
        if type(v1)==Fraction and type(v2)==Fraction:
            return v1+v2
        #return f'({v1} + {v2})'
    elif o == "-":
        if type(v1)==Fraction and type(v2)==Fraction:
            return v1-v2
        #return f'({v1} - {v2})'
    elif o == "*":
        if type(v1)==Fraction and type(v2)==Fraction:
            return v1*v2
        #return f'({v1} * {v2})'
    elif o == "/":
        if type(v1)==Fraction and type(v2)==Fraction:
            return Fraction(v1/v2)
        #return f'({v1} / {v2})'
    return Op(v1, o, v2)

r = val("root")


print(r())
