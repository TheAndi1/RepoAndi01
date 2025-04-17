# https://adventofcode.com/2015/day/3

from operator import index, truediv
from pathlib import Path



def houses_for_plan(plan):
    #mappingX = { "<" : +1, ">": -1 }
    #mappingY = { "^" : +1, "v": -1 }

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
    #current_coordinate =  (100, 100) #ginge auch: als Tupel
    from collections import namedtuple
    Coordinates = namedtuple("Coordinates", ["x", "y"])
    current_coordinates = Coordinates(100, 100)
    print(current_coordinates.x, current_coordinates.y)
    print(current_coordinates[0], current_coordinates[1])
    print(current_coordinates)

    current_coordinate = {"x":100, "y":100} #dictionary for current coordinates (always to be updated)
    supplied_houses = [str(current_coordinate["x"]) + "/" + str(current_coordinate["y"])] #list of supplied coordinates as string x/y (no duplicates possible)


    #print("start coordinates: ", str(current_coordinate["x"]) + "/" + str(current_coordinate["y"]))

    for direction in plan:
        #get next coordinates
        next_coordinates = next_house_coordinates(direction, current_coordinate["x"], current_coordinate["y"])
        #update (not add) the next coordinates in my dictionary
        current_coordinate.update({'x': next_coordinates[0], 'y': next_coordinates[1]})

        #print("new coordinates: ", str(current_coordinate["x"]) + "/" + str(current_coordinate["y"]))

        house_coordinates = f"{current_coordinate["x"]}/{current_coordinate["y"]}"
        if check_if_house_already_supplied(supplied_houses, house_coordinates) == 0:
            #add new coordinates if not exists
            #supplied_houses += [str(current_coordinate["x"]) + "/" + str(current_coordinate["y"])]
            supplied_houses.append(house_coordinates)
    return supplied_houses

assert len(houses_for_plan(">")) == 2
assert len(houses_for_plan("^>v<")) == 4
assert len(houses_for_plan("^v^v^v^v^v")) == 2

plan_of_elf = Path('day03_input.txt').read_text()
supplied_houses = houses_for_plan(plan_of_elf)
#print(supplied_houses)
print(len(supplied_houses))





#Marcels Code:

def count_houses_with_presents(directions):
    x, y = 0, 0

    # visited_houses = [x, y] # bug
    visited_houses = { (x, y) }
    #visted_houses = set()
    #visted_houses.add((x,y))

    for move in directions:
        if move == '^':
            y += 1
        elif move == 'v':
            y -= 1
        elif move == '>':
            x += 1
        elif move == '<':
            x -= 1

        #if (x, y) not in visited_houses:
        visited_houses.add((x, y))

    return len(visited_houses)

# ganz von hand, und eben ganz alt
file = open('day3_input.txt')
try:
    content = file.read()
    print(count_houses_with_presents(content))
finally:
    file.close()

# ganz von hand und falsch
file = open('day3_input.txt')
content = file.read()
print(count_houses_with_presents(content))
file.close()

# der alte weg
with open('day3_input.txt') as file:
    content = file.read()
    print(count_houses_with_presents(content))

def read_text(path):
    with open('day3_input.txt') as file:
        return file.read()

    # das hier geht nicht mehr, wenn man read_text() verwendet
    # for line in file:
    #     do_something_with(line)

# der neue weg
from pathlib import Path
print(count_houses_with_presents(Path('day3_input.txt').read_text()))

#
# memory[0] = file[0]
# ...
# memory[32*gig] = file[32*gig]
# memory[32*gig + 1] = file[32*gig + 1]

# memory[53*gig] = 'irgendwas'
# file_on_disk.write_at_offset(53*gig, 'irgendwas')
# print(memory[53*gig])
# print(file_on_disk.read_at_offset(53*gig))

print(repr([(1, 2)]))
print((3,4) in [3, 4]) # -> False
print((3,4) in [3, 4, (3,4)]) # -> True