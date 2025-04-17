# https://adventofcode.com/2015/day/5

from pathlib import Path

def check_pairs(a_string):
    position = 0
    for i in a_string:
        position += 1
        if position < len(a_string):
            pair = i + a_string[position]
            if pair.isalpha() and pair in a_string[position+1:]:
                #print(pair, a_string)
                return True

def check_overnext_char(a_string):
    position = 0
    for i in a_string:
        position += 1
        if position+1 < len(a_string) and i.isalpha() and i == a_string[position+1]:
            #print(i, a_string)
            return True

def check_if_string_is_nice(a_string):
    if check_pairs(a_string) and check_overnext_char(a_string):
        return "nice"
    else:
        return "naughty"

count_nice = 0
for a_string in Path('day05_input.txt').read_text().splitlines():
    if check_if_string_is_nice(a_string) == "nice":
        count_nice += 1

print(count_nice)

assert(check_if_string_is_nice("qjhvhtzxzqqjkmpb")) == "nice"
assert(check_if_string_is_nice("xxyxx")) == "nice"
assert(check_if_string_is_nice("uurcxstgmygtbstg")) == "naughty"
assert(check_if_string_is_nice("ieodomkazucvgmuy")) == "naughty"