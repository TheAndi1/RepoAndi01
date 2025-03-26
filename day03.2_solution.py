# https://adventofcode.com/2015/day/3

from pathlib import Path

def houses_for_plan(plan):

    def next_house_coordinates(direction, x, y):
        if direction == "^": y += 1
        elif direction == "v": y -= 1
        elif direction == "<": x -= 1
        elif direction == ">": x += 1
        return x, y

    def check_if_house_already_supplied(supplied_houses, next_coordinates):
        already_supplied = 0
        for i in supplied_houses:
            if i == next_coordinates:
                already_supplied = 1
        return already_supplied

    current_coordinate_W = {"x":100, "y":100} #dictionary for current coordinates (always to be updated)
    current_coordinate_R = {"x": 100, "y": 100}  # dictionary for current coordinates (always to be updated)

    start = f"{current_coordinate_W['x']}/{current_coordinate_W['y']}"
    supplied_houses = [start]

    next_deliverer = "W"
    for direction in plan:

        if next_deliverer == "W":
            next_coordinates_W = next_house_coordinates(direction, current_coordinate_W["x"], current_coordinate_W["y"])
            current_coordinate_W.update({'x': next_coordinates_W[0], 'y': next_coordinates_W[1]})
            house_coordinates = f"{current_coordinate_W['x']}/{current_coordinate_W['y']}"
            next_deliverer = "R"
        elif next_deliverer == "R":
            next_coordinates_R = next_house_coordinates(direction, current_coordinate_R["x"], current_coordinate_R["y"])
            current_coordinate_R.update({'x': next_coordinates_R[0], 'y': next_coordinates_R[1]})
            house_coordinates = f"{current_coordinate_R['x']}/{current_coordinate_R['y']}"
            next_deliverer = "W"


        if check_if_house_already_supplied(supplied_houses, house_coordinates) == 0:
            supplied_houses.append(house_coordinates)


    return supplied_houses

assert len(houses_for_plan("^v")) == 3
assert len(houses_for_plan("^>v<")) == 3
assert len(houses_for_plan("^v^v^v^v^v")) == 11

plan_of_elf = Path('day03_input.txt').read_text()
supplied_houses = houses_for_plan(plan_of_elf)
print(len(supplied_houses))





