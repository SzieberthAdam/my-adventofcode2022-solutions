import pathlib

example = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

elines = example.split("\n")

ilines = []
with pathlib.Path("input.txt").open() as _f:
    ilines = [_line.rstrip("\n") for _line in _f.readlines()]

e_s = e_pair_sections = [[set(range(int(s.split("-")[0]), int(s.split("-")[1])+1)) for s in line.split(",")] for line in elines]
i_s = i_pair_sections = [[set(range(int(s.split("-")[0]), int(s.split("-")[1])+1)) for s in line.split(",")] for line in ilines]

ftest = lambda pair: 1 - (bool(pair[1]-pair[0]) and bool(pair[0]-pair[1]))

e_f = e_num_fully_contains = sum(ftest(pair) for pair in e_s)
i_f = i_num_fully_contains = sum(ftest(pair) for pair in i_s)

otest = lambda pair: int(bool(pair[0] & pair[1]))

e_o = e_num_overlaps = sum(otest(pair) for pair in e_s)
i_o = i_num_overlaps = sum(otest(pair) for pair in i_s)
