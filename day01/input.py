import pathlib


inventories = []
inventory = []
with pathlib.Path("input.txt").open() as _f:
    for _line in _f.readlines():
        _valstr = _line.rstrip("\n")
        if _valstr:
            inventory.append(int(_valstr))
        else:
            inventories.append(inventory)
            inventory = []
    else:
        if inventory:
            inventories.append(inventory)
            inventory = []

inventory_calories = [sum(inventory) for inventory in inventories]

highest_carried_calories = sorted(inventory_calories)[-1]

top3_carried_calories = sum(sorted(inventory_calories)[-3:])
