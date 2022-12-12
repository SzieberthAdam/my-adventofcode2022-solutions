import pathlib

example = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

elines = example.split("\n")

ilines = []
with pathlib.Path("input.txt").open() as _f:
    ilines = [_line.rstrip("\n") for _line in _f.readlines()]

ei = elines.index("")
ii = ilines.index("")

estacklines = elines[:ei]
istacklines = ilines[:ii]

eproclines = elines[ei+1:]
iproclines = ilines[ii+1:]

eproc = [[int(s) for s in line.split() if s.isdecimal()] for line in eproclines]
iproc = [[int(s) for s in line.split() if s.isdecimal()] for line in iproclines]

enumstacks = max({item for sublist in eproc for item in sublist[1:]}) # first integer is movecount and should get ignored
inumstacks = max({item for sublist in iproc for item in sublist[1:]})

estacks = [[] for _ in range(enumstacks)]
istacks = [[] for _ in range(inumstacks)]

stacks = estacks
stacklines = estacklines

for line in reversed(stacklines[:-1]):
    crates = line[1:len(line):4]
    for i, crate in enumerate(crates):
        if crate != " ":
            stacks[i].append(crate)

import copy
orig_estacks = copy.deepcopy(estacks)

proc = eproc

for movecnt, fromstack, tostack in proc:
    for i in range(movecnt):
        crate = stacks[fromstack-1].pop()
        stacks[tostack-1].append(crate)

stacks = istacks
stacklines = istacklines

for line in reversed(stacklines[:-1]):
    crates = line[1:len(line):4]
    for i, crate in enumerate(crates):
        if crate != " ":
            stacks[i].append(crate)

orig_istacks = copy.deepcopy(istacks)

proc = iproc

for movecnt, fromstack, tostack in proc:
    for i in range(movecnt):
        crate = stacks[fromstack-1].pop()
        stacks[tostack-1].append(crate)


emsg1 = "".join(stack[-1] for stack in estacks)
imsg1 = "".join(stack[-1] for stack in istacks)

estacks1 = estacks
istacks1 = istacks
estacks2 = copy.deepcopy(orig_estacks)
istacks2 = copy.deepcopy(orig_istacks)


stacks = estacks2
proc = eproc

for movecnt, fromstack, tostack in proc:
    crates = stacks[fromstack-1][-movecnt:]
    stacks[fromstack-1] = stacks[fromstack-1][:-movecnt]
    stacks[tostack-1].extend(crates)

stacks = istacks2
proc = iproc

for movecnt, fromstack, tostack in proc:
    crates = stacks[fromstack-1][-movecnt:]
    stacks[fromstack-1] = stacks[fromstack-1][:-movecnt]
    stacks[tostack-1].extend(crates)

emsg2 = "".join(stack[-1] for stack in estacks2)
imsg2 = "".join(stack[-1] for stack in istacks2)
