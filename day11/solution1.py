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
        m = collections.deque([int(x) for x in line.split(": ")[1].split(", ")])
        items.append(m)
    if line.startswith("  Operation: "):
        if line.startswith("  Operation: new = old * "):
            ops.append(["*", line.split()[-1]])
            #ops.append(lambda x: x * int(line.split()[-1]))
        elif line.startswith("  Operation: new = old + "):
            ops.append(["+", line.split()[-1]])
            #ops.append(lambda x: x + int(line.split()[-1]))
        else:
            raise Exception
    if line.startswith("  Test: "):
        if line.startswith("  Test: divisible by "):
            tests.append(["!%", int(line.split()[-1])])
            #tests.append(lambda x: 0 == (x % int(line.split()[-1])))
        else:
            raise Exception
    if line.startswith("    If true: throw to monkey "):
        truetarget.append(int(line.split()[-1]))
    if line.startswith("    If false: throw to monkey "):
        falsetarget.append(int(line.split()[-1]))

rounds = 20
divider = 3

inspections = [0] * len(items)

for ri in range(rounds):

    print(f'=== ROUND {ri+1} ===')

    for mi, m in enumerate(items):
        print(f'Monkey {mi}')
        while m:
            w0 = m.popleft()
            print(f'  Monkey inspects an item with a worry level of {w0}.')
            x = w0 if ops[mi][1] == "old" else int(ops[mi][1])
            if ops[mi][0] == "*":
                w1 = w0 * x
                print(f'    Worry level is multiplied by {x} to {w1}.')
            elif ops[mi][0] == "+":
                w1 = w0 + x
                print(f'    Worry level increases by {x} to {w1}.')
            inspections[mi] += 1
            w2 = w1 // divider
            print(f'    Monkey gets bored with item. Worry level is divided by {divider} to {w2}.')
            test = (0 == (w2 % tests[mi][1]))
            if test:
                print(f'    Current worry level is divisible by {tests[mi][1]}.')
                mt = truetarget[mi]
            else:
                print(f'    Current worry level is not divisible by {tests[mi][1]}.')
                mt = falsetarget[mi]
            items[mt].append(w2)
            print(f'    Item with worry level {w2} is thrown to monkey {mt}.')

    print()

    for mi, m in enumerate(items):
        print(f'Monkey {mi}: {", ".join([str(x) for x in m])}')

    print()

for mi, v in enumerate(inspections):
    print(f'Monkey {mi} inspected items {v} times.')

mostactive = 2

monkeybusiness = math.prod(sorted(inspections)[-mostactive:])

print()
print(f'Answer 1: {monkeybusiness}')
