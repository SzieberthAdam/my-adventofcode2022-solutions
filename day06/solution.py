buffers = [
    """mjqjpqmgbljsphdztnvjfqwrcgsmlb""",
    """bvwbjplbgvbhsrlpgdmjqwftvncz""",
    """nppdvjthqldpwncqszvftbrmjlhg""",
    """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg""",
    """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw""",
]

import pathlib
with pathlib.Path("input.txt").open() as _f:
    inp = _f.read()

buffers.append(inp)

ndistinct = 4

for buffer in buffers:
    print(f'{buffer[:6]}...')
    import collections
    d = collections.deque()
    for n, c in enumerate(buffer, 1):
        d.append(c)
        if ndistinct+1 <= len(d):
            d.popleft()
        if ndistinct == len(d) and ndistinct == len(set(d)):
            print(n)
            break

n1 = n


print("PART2")

ndistinct = 14

for buffer in buffers:
    print(f'{buffer[:6]}...')
    import collections
    d = collections.deque()
    for n, c in enumerate(buffer, 1):
        d.append(c)
        if ndistinct+1 <= len(d):
            d.popleft()
        if ndistinct == len(d) and ndistinct == len(set(d)):
            print(n)
            break

n2 = n
