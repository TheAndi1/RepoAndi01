#https://adventofcode.com/2015/day/6
from idlelib.config_key import translate_key
from os import WCONTINUED
from pathlib import Path
import numpy as np
import re


light_grid = np.zeros((1000, 1000))


def set_grid_to_default():
    for i in range(len(light_grid)):
        for j in range(len(light_grid[i])):
            light_grid[i][j] = 0

def count_lights():
    lights_on = 0
    for row in light_grid:
        for light in row:
            if light == 1:
                lights_on += 1
    return lights_on


def find_first_number(text):
    for index, character in enumerate(text):
        if character.isdigit():
            return index
    return -1


def find_first_comma(text):
    for index, character in enumerate(text):
        if character == ",":
            return index
    return -1


def find_first_space(text):
    for index, character in enumerate(text):
        if character == " ":
            return index
    return -1


def split_text_line(text_line):
    process = text_line[:find_first_number(text_line) - 1]
    text_line = text_line[find_first_number(text_line):]
    coord1 = (int(text_line[:find_first_comma(text_line)]), int(text_line[find_first_comma(text_line) + 1:find_first_space(text_line)]))
    text_line = text_line[find_first_space(text_line)+1:][find_first_space(text_line[find_first_space(text_line) + 1:]) + 1:]
    coord2 = (int(text_line[:find_first_comma(text_line)]), int(text_line[find_first_comma(text_line) + 1:]))
    return process, coord1, coord2


def process_text_line(coord1, coord2, process):
    for row_index, row in enumerate(light_grid):
        for light_index, light in enumerate(row):
            if row_index >= coord1[0] and row_index <= coord2[0]:
                if light_index >= coord1[1] and light_index <= coord2[1]:
                    match process:
                        case "turn on":
                            light_grid[row_index][light_index] = 1
                        case "turn off":
                            light_grid[row_index][light_index] = 0
                        case "toggle":
                            if light == 0:
                                light_grid[row_index][light_index] = 1
                            elif light == 1:
                                light_grid[row_index][light_index] = 0
                        case _:
                            print("invalid")


def process_text_input(text_input):
    for text_line in text_input.splitlines():
        process, coord1, coord2 = split_text_line(text_line)
        process_text_line(coord1, coord2, process)
    return_count = count_lights()
    print(return_count)
    set_grid_to_default()
    return return_count



content = Path('day06_input.txt').read_text()
process_text_input(content)


assert(process_text_input("turn on 0,0 through 999,999")) == 1000000
assert(process_text_input("toggle 0,0 through 999,0")) == 1000
assert(process_text_input("turn off 499,499 through 500,500")) == 0
