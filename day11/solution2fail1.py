import collections
import math
import pathlib
import sys

class SieveOfEratosthenes:

    def __init__(self):
        self.n = 1
        self.next_composite = collections.defaultdict(list)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.n += 1
            n = self.n
            prime_divisors = self.next_composite.get(n)
            if prime_divisors is None:
                p = n  # n is prime
                self.next_composite[n+p].append(p)
                return n
            else:
                for p in prime_divisors:
                    self.next_composite[n+p].append(p)
                del self.next_composite[n]

def unique_factorization(v):
    sieve = SieveOfEratosthenes()
    factors = []
    for p in sieve:
        mo = 0
        while not mo:
            di, mo = divmod(v, p)
            if not mo:
                factors.append(p)
                v = di
        if v < p:
            break
    return factors

def composite_factorization(v):
    def subgen(factors):
        prev = None
        v = None
        for f in factors:
            if f != prev:
                if prev is not None:
                    yield v
                prev = v = f
            else:
                v *= f
        else:
            if prev is not None:
                yield v
    return list(subgen(unique_factorization(v)))


with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]


items = []
ops = []
tests = []
truetarget = []
falsetarget = []
for line in lines:
    if line.startswith("  Starting items: "):
        m = collections.deque([tuple(unique_factorization(int(x))) for x in line.split(": ")[1].split(", ")])
        items.append(m)
    if line.startswith("  Operation: "):
        x = line.split()[-1]
        x = x if line.split()[-1] == "old" else int(line.split()[-1])
        if line.startswith("  Operation: new = old * "):
            ops.append(["*", x if x == "old" else tuple(unique_factorization(x))])
        elif line.startswith("  Operation: new = old + "):
            ops.append(["+", x])
        else:
            raise Exception
    if line.startswith("  Test: "):
        if line.startswith("  Test: divisible by "):
            tests.append(["!%", tuple(unique_factorization(int(line.split()[-1])))])
        else:
            raise Exception
    if line.startswith("    If true: throw to monkey "):
        truetarget.append(int(line.split()[-1]))
    if line.startswith("    If false: throw to monkey "):
        falsetarget.append(int(line.split()[-1]))

rounds = 10000
divider = 3

inspections = [0] * len(items)

for ri in range(rounds):

    #if ri == 10: raise Exception
    print(f'=== ROUND {ri+1} ===')

    for mi, m in enumerate(items):
        print(f'Monkey {mi}')
        while m:
            w0 = m.popleft()
            # print(f'  Monkey inspects an item with a worry level of {w0}.')
            if ops[mi][0] == "*":
                if ops[mi][1] == "old":
                    w1 = tuple(sorted(w0+w0))
                else:
                    w1 = tuple(sorted(w0+ops[mi][1]))
            elif ops[mi][0] == "+":
                if ops[mi][1] == "old":
                    w1 = tuple(sorted(w0+(2,)))
                else:
                    print(f'before: {w0} + {ops[mi][1]}')
                    w1 = tuple(unique_factorization(math.prod(w0) + ops[mi][1]))
                    print(f'after: {w1}')
            inspections[mi] += 1

            w1c = collections.Counter(w1)
            tc = collections.Counter(tests[mi][1])
            test = all(tf <= w1c[x] for x, tf in tc.items())
            if test:
                #print(f'    Current worry level is divisible by {tests[mi][1]}.')
                mt = truetarget[mi]
            else:
                #print(f'    Current worry level is not divisible by {tests[mi][1]}.')
                mt = falsetarget[mi]
            items[mt].append(w1)
            #print(f'    Item with worry level {w2} is thrown to monkey {mt}.')

#
#     #print()
#
#     #for mi, m in enumerate(items):
#     #    print(f'Monkey {mi}: {", ".join([str(x) for x in m])}')
#
#     #print()
#
#     if ri+1 == 1 or ri+1 == 20 or (((ri+1) % 1000) == 0):
#         print(f'== After round {ri+1} ==')
#         for mi, v in enumerate(inspections):
#             print(f'Monkey {mi} inspected items {v} times.')
#         print()
#
# mostactive = 2
#
# monkeybusiness = math.prod(sorted(inspections)[-mostactive:])
#
# print()
# print(f'Answer 2: {monkeybusiness}')
#
#
# for mi, m in enumerate(items):
#     print(f'Monkey {mi}: {", ".join([str(x) for x in m])}')
