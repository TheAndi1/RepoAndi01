# https://adventofcode.com/2015/day/3

from operator import index, truediv
from pathlib import Path




plan_of_elf = Path('day03_input.txt').read_text()


#Functions
def next_house_coordinates(direction, x, y):
    #print("Übergabe1: ", direction, x, y)
    if direction == "^": y += 1
    elif direction == "v": y -= 1
    elif direction == "<": x -= 1
    elif direction == ">": x += 1
    return x, y

def check_if_house_already_supplied(supplied_houses, next_coordinates):
    already_supplied = 0
    #print("übergabe2: supplied houses: ", supplied_houses, "next coordinates", next_coordinates)
    for i in supplied_houses:
        if i == next_coordinates:
            already_supplied = 1
    return already_supplied

#main
#variables
current_coordinate = {"x":100, "y":100} #dictionary for current coordinates (always to be updated)
supplied_houses = [str(current_coordinate["x"]) + "/" + str(current_coordinate["y"])] #list of supplied coordinates as string x/y (no duplicates possible)

#print("start coordinates: ", str(current_coordinate["x"]) + "/" + str(current_coordinate["y"]))

for direction in plan_of_elf:
    #get next coordinates
    next_coordinates = next_house_coordinates(direction, current_coordinate["x"], current_coordinate["y"])
    #update (not add) the next coordinates in my dictionary
    current_coordinate.update({'x': next_coordinates[0], 'y': next_coordinates[1]})

    #print("new coordinates: ", str(current_coordinate["x"]) + "/" + str(current_coordinate["y"]))

    if check_if_house_already_supplied(supplied_houses, str(current_coordinate["x"]) + "/" + str(current_coordinate["y"])) == 0:
        #add new coordinates if not exists
        supplied_houses += [str(current_coordinate["x"]) + "/" + str(current_coordinate["y"])]

#print(supplied_houses)
print(len(supplied_houses))

