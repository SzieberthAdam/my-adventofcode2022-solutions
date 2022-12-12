import pathlib

lines = []
with pathlib.Path("input.txt").open() as _f:
    lines = [_line.rstrip("\n") for _line in _f.readlines()]


scoretable1 = {
    "AX": 1+3,
    "AY": 2+6,
    "AZ": 3+0,
    "BX": 1+0,
    "BY": 2+3,
    "BZ": 3+6,
    "CX": 1+6,
    "CY": 2+0,
    "CZ": 3+3,
}

scores1 = []
for _line in lines:
    _opp, _my = _line.split()
    _score = scoretable1[_opp+_my]
    scores1.append(_score)

total_score1 = sum(scores1)


transtable2 = {
    "AX": "AZ",
    "AY": "AX",
    "AZ": "AY",
    "BX": "BX",
    "BY": "BY",
    "BZ": "BZ",
    "CX": "CY",
    "CY": "CZ",
    "CZ": "CX",
}

scores2 = []
for _line in lines:
    _opp, _my = _line.split()
    _score = scoretable1[transtable2[_opp+_my]]
    scores2.append(_score)

total_score2 = sum(scores2)
