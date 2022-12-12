import pathlib

example = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

elines = example.split("\n")

ilines = []
with pathlib.Path("input.txt").open() as _f:
    ilines = [_line.rstrip("\n") for _line in _f.readlines()]

erc = e_rucksack_compartments = [[line[:len(line)//2], line[len(line)//2:]] for line in elines]
irc = i_rucksack_compartments = [[line[:len(line)//2], line[len(line)//2:]] for line in ilines]

ers = e_rucksack_shares = [set(r[0]) & set(r[1]) for r in erc]
irs = i_rucksack_shares = [set(r[0]) & set(r[1]) for r in irc]

def prio(c):
    o = ord(c)
    if (ord("a") <= o <= ord("z")):
        return o - ord("a") + 1
    if (ord("A") <= o <= ord("Z")):
        return o - ord("A") + 27

ep = e_sum_of_priorities = sum(sum(prio(c) for c in S) for S in ers)
ip = i_sum_of_priorities = sum(sum(prio(c) for c in S) for S in irs)

GROUPSIZE = 3

eg = e_groups = [elines[i:i+GROUPSIZE] for i in range(0, len(elines), GROUPSIZE)]
ig = i_groups = [ilines[i:i+GROUPSIZE] for i in range(0, len(ilines), GROUPSIZE)]

egs = e_group_shares = [set(r[0]) & set(r[1]) & set(r[2]) for r in eg]
igs = i_group_shares = [set(r[0]) & set(r[1]) & set(r[2]) for r in ig]

egp = e_group_sum_of_priorities = sum(sum(prio(c) for c in S) for S in egs)
igp = i_group_sum_of_priorities = sum(sum(prio(c) for c in S) for S in igs)
