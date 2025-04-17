# https://adventofcode.com/2015/day/3

from pathlib import Path

def next_house_coordinates(direction, x, y):
    if direction == "^": y += 1
    elif direction == "v": y -= 1
    elif direction == "<": x -= 1
    elif direction == ">": x += 1
    return {'x': x, 'y': y}

def houses_for_plan(plan):
    current_coordinate = current_coordinate_r = current_coordinate_w = {"x":100, "y":100} #dictionary for current coordinates (always to be updated)
    supplied_houses = [current_coordinate]

    next_deliverer = "W"
    for direction in plan:
        if next_deliverer == "W":
            current_coordinate = current_coordinate_w = next_house_coordinates(direction, current_coordinate_w["x"], current_coordinate_w["y"])
            next_deliverer = "R"
        elif next_deliverer == "R":
            current_coordinate = current_coordinate_r = next_house_coordinates(direction, current_coordinate_r["x"], current_coordinate_r["y"])
            next_deliverer = "W"

        if current_coordinate not in supplied_houses:
            supplied_houses.append(current_coordinate)

    return supplied_houses

assert len(houses_for_plan("^v")) == 3
assert len(houses_for_plan("vvvv")) == 3
assert len(houses_for_plan("^>v<")) == 3
assert len(houses_for_plan("^v^v^v^v^v")) == 11


plan_of_elf = Path('day03_input.txt').read_text()
supplied_houses = houses_for_plan(plan_of_elf)
assert len(supplied_houses) == 2631
print(len(supplied_houses))





