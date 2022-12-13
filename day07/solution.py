import pathlib

example = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

elines = example.split("\n")

ilines = []
with pathlib.Path("input.txt").open() as _f:
    ilines = [_line.rstrip("\n") for _line in _f.readlines()]

import collections

lines = elines

subdirs = collections.defaultdict(set)
files = collections.defaultdict(set)
size = {}
dirsize = collections.defaultdict(lambda: 0)
dirstack = ["/"]
mode = ""
for line in lines:
    if line.startswith("$"):
        if line == "$ ls":
            mode = "ls"
        elif line == "$ cd /":
            mode = "cd"
            dirstack = ["/"]
        elif line == "$ cd ..":
            mode = "cd"
            dirstack = dirstack[:-1]
        elif line.startswith("$ cd "):
            mode = "cd"
            dirstack.append(line[len("$ cd "):])
    elif mode == "ls":
        if line.startswith("dir "):
            dname = line[len("dir "):]
            path = tuple(dirstack) + (dname,)
            subdirs[tuple(dirstack)].add(path)
        else:
            fsizestr, fname = line.split(" ", 1)
            path = tuple(dirstack) + (fname,)
            files[tuple(dirstack)].add(path)
            fsize = int(fsizestr)
            size[path] = fsize
            for i in range(len(dirstack)):
                dpath = tuple(dirstack[:len(dirstack)-i])
                dirsize[dpath] += fsize

for path, size in dirsize.items():
    print(f'{"/".join(path)} -> {size}')

answer1e = sum(size for path, size in dirsize.items() if size <= 100000)

print(f'Answer 1 (example): {answer1e}')

import copy

edirsize = copy.deepcopy(dirsize)


lines = ilines

subdirs = collections.defaultdict(set)
files = collections.defaultdict(set)
size = {}
dirsize = collections.defaultdict(lambda: 0)
dirstack = ["/"]
mode = ""
for line in lines:
    if line.startswith("$"):
        if line == "$ ls":
            mode = "ls"
        elif line == "$ cd /":
            mode = "cd"
            dirstack = ["/"]
        elif line == "$ cd ..":
            mode = "cd"
            dirstack = dirstack[:-1]
        elif line.startswith("$ cd "):
            mode = "cd"
            dirstack.append(line[len("$ cd "):])
    elif mode == "ls":
        if line.startswith("dir "):
            dname = line[len("dir "):]
            path = tuple(dirstack) + (dname,)
            subdirs[tuple(dirstack)].add(path)
        else:
            fsizestr, fname = line.split(" ", 1)
            path = tuple(dirstack) + (fname,)
            files[tuple(dirstack)].add(path)
            fsize = int(fsizestr)
            size[path] = fsize
            for i in range(len(dirstack)):
                dpath = tuple(dirstack[:len(dirstack)-i])
                dirsize[dpath] += fsize

#for path, size in dirsize.items():
#    print(f'{"/".join(path)} -> {size}')

answer1 = sum(size for path, size in dirsize.items() if size <= 100000)

print(f'Answer 1: {answer1}')

idirsize = copy.deepcopy(dirsize)

totalspace = 70000000
reqspace = 30000000

dirsize = edirsize

freespace = totalspace - dirsize[("/",)]

for path in sorted(dirsize, key=dirsize.get):
    size = dirsize[path]
    print(path, size)
    if reqspace < freespace + size:
        print("THIS")
        break


dirsize = idirsize

freespace = totalspace - dirsize[("/",)]

for path in sorted(dirsize, key=dirsize.get):
    size = dirsize[path]
    if reqspace < freespace + size:
        print(f'Answer 2: {size}')
        break
