# https://adventofcode.com/2015/day/5

from operator import index, truediv
from pathlib import Path

def check_vowels(a_string):
    return a_string.lower().count("a") + a_string.lower().count("e") + a_string.lower().count("i") + a_string.lower().count("o") + a_string.lower().count("u")

def check_doubles(a_string):
    position = 0
    for i in a_string:
        position += 1
        if position < len(a_string) and i.isalpha() and i == a_string[position]:
            return True


def check_forbidden_content(a_string):
    if "ab" not in a_string and "cd" not in a_string and "pq" not in a_string and "xy" not in a_string:
        return True

def check_if_string_is_nice(a_string):
    if check_vowels(a_string) >= 3 and check_doubles(a_string) and check_forbidden_content(a_string):
        return "nice"
    else:
        return "naughty"

count_nice = 0
for a_string in Path('day05_input.txt').read_text().splitlines():
    if check_if_string_is_nice(a_string) == "nice":
        count_nice += 1

print(count_nice)

assert(check_if_string_is_nice("ugknbfddgicrmopn")) == "nice"
assert(check_if_string_is_nice("aaa")) == "nice"
assert(check_if_string_is_nice("jchzalrnumimnmhp")) == "naughty"
assert(check_if_string_is_nice("haegwjzuvuyypxyu")) == "naughty"
assert(check_if_string_is_nice("dvszwmarrgswjxmb")) == "naughty"
