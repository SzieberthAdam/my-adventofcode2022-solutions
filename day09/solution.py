example = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

elines = example.split("\n")

ilines = []
import pathlib
with pathlib.Path("input.txt").open() as _f:
    ilines = [_line.rstrip("\n") for _line in _f.readlines()]


s = [0, 0]
T = [0, 0]
H = [0, 0]
S_Tpos = {(0, 0),}
lines = elines

print("== Initial State ==\n")

def show(s, H, T, width, height):
    rows = []
    for ri in range(height-1, -1, -1):
        row = ["."] * width
        for ci in range(width):
            if tuple(s) == (ri, ci): row[ci] = "s"
            if tuple(T) == (ri, ci): row[ci] = "T"
            if tuple(H) == (ri, ci): row[ci] = "H"
        rows.append("".join(row))
    return "\n".join(rows)

print(show(s, H, T, 6, 5))

def apply1(d):
    if d == "R":
        H[1] += 1
    elif d == "L":
        H[1] -= 1
    elif d == "U":
        H[0] += 1
    elif d == "D":
        H[0] -= 1
    dist = max(abs(H[0]-T[0]), abs(H[1]-T[1]))
    if 1 < dist:
        for i in range(2):
            if T[i] < H[i]:
                T[i] += 1
            elif T[i] > H[i]:
                T[i] -= 1
        S_Tpos.add(tuple(T))

for line in lines:
    print(f'== {line} ==')
    print()
    d = line.split()[0]
    c = int(line.split()[1])
    for _ in range(c):
        apply1(d)
        print(show(s, H, T, 6, 5))
        print()


print(f'Answer 1 (example): {len(S_Tpos)}')

s = [0, 0]
T = [0, 0]
H = [0, 0]
S_Tpos = {(0, 0),}
lines = ilines

for line in lines:
    d = line.split()[0]
    c = int(line.split()[1])
    for _ in range(c):
        apply1(d)

print(f'Answer 1: {len(S_Tpos)}')

example2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

e2lines = example2.split("\n")

lines = e2lines
K = [[0, 0] for _ in range(10)]
S_Tpos = {(0, 0),}

def apply1_2(d):
    if d == "R":
        K[0][1] += 1
    elif d == "L":
        K[0][1] -= 1
    elif d == "U":
        K[0][0] += 1
    elif d == "D":
        K[0][0] -= 1
    for k in range(1,10):
        dist = max(abs(K[k-1][0]-K[k][0]), abs(K[k-1][1]-K[k][1]))
        if 1 < dist:
            for i in range(2):
                if K[k][i] < K[k-1][i]:
                    K[k][i] += 1
                elif K[k][i] > K[k-1][i]:
                    K[k][i] -= 1
    S_Tpos.add(tuple(K[-1]))

for line in lines:
    d = line.split()[0]
    c = int(line.split()[1])
    for _ in range(c):
        apply1_2(d)

print(f'Answer 2 (example): {len(S_Tpos)}')

lines = ilines
K = [[0, 0] for _ in range(10)]
S_Tpos = {(0, 0),}

for line in lines:
    d = line.split()[0]
    c = int(line.split()[1])
    for _ in range(c):
        apply1_2(d)

print(f'Answer 2: {len(S_Tpos)}')
