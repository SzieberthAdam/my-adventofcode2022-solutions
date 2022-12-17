import json
import math
import pathlib
import sys

import pyclipper

with pathlib.Path(sys.argv[1]).open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]

S = set()

coords = [[float(b.strip("xy=")) for a in line.split(":") for b in a.strip(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ").split(", ")] for line in lines]

minv = 0.0
maxv = float(sys.argv[2]) if 3 <= len(sys.argv) else 4000000.0
#maxv = 20.0

subjects0 = [[[minv, minv], [minv, maxv], [maxv, maxv], [maxv, minv]]]

coords0 = []
coords1 = list(coords)

while coords1:
    coords0 = coords1
    coords1 = []
    for c in coords0:
        x1, y1, x2, y2 = c
        pc = pyclipper.Pyclipper()
        pc.AddPaths(pyclipper.scale_to_clipper(subjects0), pyclipper.PT_SUBJECT, True)
        dist = abs(x1-x2) + abs(y1-y2)
        clip = [[x1-dist, y1], [x1, y1-dist], [x1+dist, y1], [x1, y1+dist]]
        print(f'coords: {(x1, y1, x2, y2)}')
        print(f'clip: {clip}')
        pc.AddPath(pyclipper.scale_to_clipper(clip), pyclipper.PT_CLIP, True)
        subjects1 = pyclipper.scale_from_clipper(pc.Execute(pyclipper.CT_DIFFERENCE))
        for p in subjects1:
            print(p)
        subjects0 = subjects1
        #if len(subjects1) == 1:
        #    subjects0 = subjects1
        #else:
        #    coords1.append(c)
        #    print("deferred")
        print()

print(subjects0)
for p in subjects0[0]:
    print(p)

print()
from decimal import Decimal as D
print(D(2713145)*D(4000000) + D(3132904))
