example = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

elines = example.split("\n")

ilines = []
import pathlib
with pathlib.Path("input.txt").open() as _f:
    ilines = [_line.rstrip("\n") for _line in _f.readlines()]


cycles = {"addx": 2, "noop": 1}

lines = elines
x = 1
c = 0
i = -1
p0 = 0
ci = 1
op, v = "", 0
totsigstrength = 0
while True:
    c += 1
    if c == ci:
        if op == "addx": x += v
        i += 1
        try:
            op, _, v = lines[i].partition(" ")
            ci += cycles[op]
        except IndexError:
            break
        else:
            if v: v = int(v)
    sigstrength = c * x
    if c % 40 == 20:
        totsigstrength += sigstrength
        print(f'cycle: {c}; x: {x}; signal strength: {sigstrength} (total: {totsigstrength})')


print(f'Answer 1 (example): {totsigstrength}')

print()

lines = ilines
x = 1
c = 0
i = -1
p0 = 0
ci = 1
op, v = "", 0
totsigstrength = 0
while True:
    c += 1
    if c == ci:
        if op == "addx": x += v
        i += 1
        try:
            op, _, v = lines[i].partition(" ")
            ci += cycles[op]
        except IndexError:
            break
        else:
            if v: v = int(v)
    sigstrength = c * x
    if c % 40 == 20:
        totsigstrength += sigstrength
        print(f'cycle: {c}; x: {x}; signal strength: {sigstrength} (total: {totsigstrength})')

print(f'Answer 1: {totsigstrength}')

sprw = 3
crtw = 40
crth = 6

lines = elines
x = 1
c = 0
i = -1
p0 = 0
ci = 1
op, v = "", 0
rows = [[" "] * crtw for _ in range(crth)]
while True:
    c += 1
    if c == ci:
        if op == "addx": x += v
        i += 1
        try:
            op, _, v = lines[i].partition(" ")
            ci += cycles[op]
        except IndexError:
            break
        else:
            if v: v = int(v)
    c1, c2 = divmod(c-1, crtw * crth)
    ri, pi = divmod(c2, crtw)
    if ((x-(sprw-1)//2) <= pi <= (x+(sprw-1)//2)):
        rows[ri][pi] = "#"
    else:
        rows[ri][pi] = "."
    print(f'cycle: {c}; frame: {c1+1}; row: {ri}; col: {pi}; x: {x}\n{"".join(rows[ri])}')

print()

print("\n".join("".join(row) for row in rows))

lines = ilines
x = 1
c = 0
i = -1
p0 = 0
ci = 1
op, v = "", 0
rows = [[" "] * crtw for _ in range(crth)]
while True:
    c += 1
    if c == ci:
        if op == "addx": x += v
        i += 1
        try:
            op, _, v = lines[i].partition(" ")
            ci += cycles[op]
        except IndexError:
            break
        else:
            if v: v = int(v)
    c1, c2 = divmod(c-1, crtw * crth)
    ri, pi = divmod(c2, crtw)
    if ((x-(sprw-1)//2) <= pi <= (x+(sprw-1)//2)):
        rows[ri][pi] = "#"
    else:
        rows[ri][pi] = "."

print()

print("\n".join("".join(row) for row in rows))
