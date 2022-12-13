import collections
import math
import pathlib
import sys


with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]


items = []
ops = []
tests = []
truetarget = []
falsetarget = []
for line in lines:
    if line.startswith("  Starting items: "):
        m = collections.deque([[["+", int(x)]] for x in line.split(": ")[1].split(", ")])
        items.append(m)
    if line.startswith("  Operation: "):
        x = line.split()[-1]
        x = x if line.split()[-1] == "old" else int(line.split()[-1])
        if line.startswith("  Operation: new = old * "):
            ops.append(["*", x])
        elif line.startswith("  Operation: new = old + "):
            ops.append(["+", x])
        else:
            raise Exception
    if line.startswith("  Test: "):
        if line.startswith("  Test: divisible by "):
            tests.append(["!%", int(line.split()[-1])])
        else:
            raise Exception
    if line.startswith("    If true: throw to monkey "):
        truetarget.append(int(line.split()[-1]))
    if line.startswith("    If false: throw to monkey "):
        falsetarget.append(int(line.split()[-1]))

rounds = 10000

inspections = [0] * len(items)

for ri in range(rounds):

    for mi, m in enumerate(items):
        while m:
            w0 = m.popleft()
            if ops[mi][0] == "*":
                if ops[mi][1] == "old":
                    w1 = w0 + [["**", 2]]
                else:
                    w1 = w0 + [ops[mi]]
            elif ops[mi][0] == "+":
                if ops[mi][1] == "old":
                    w1 = w0 + [["*", 2]]
                else:
                    w1 = w0 + [ops[mi]]
            inspections[mi] += 1

            di = tests[mi][1]
            mo = 0

            for op, v in w1:
                if op == "+":
                    mo += v
                elif op == "*":
                    mo *= v
                elif op == "**":
                    mo = mo**v
                mo %= di

            test = (mo==0)
            if test:
                mt = truetarget[mi]
            else:
                mt = falsetarget[mi]
            items[mt].append(w1)

    if ri+1 == 1 or ri+1 == 20 or (((ri+1) % 1000) == 0):
        print(f'== After round {ri+1} ==')
        for mi, v in enumerate(inspections):
            print(f'Monkey {mi} inspected items {v} times.')
        print()

mostactive = 2

monkeybusiness = math.prod(sorted(inspections)[-mostactive:])

print()
print(f'Answer 2: {monkeybusiness}')
