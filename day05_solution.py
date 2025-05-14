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
    return False


def check_forbidden_content(a_string):
    return (
        "ab" not in a_string
        and "cd" not in a_string
        and "pq" not in a_string
        and "xy" not in a_string
    )

    forbidden_content = ['ab', 'cd', 'pq', 'xy']
    return all(map(lambda each: each not in a_string, forbidden_content))

    not_ab = "ab" not in a_string
    not_cd = "cd" not in a_string
    not_pq = "pq" not in a_string
    not_xy = "xy" not in a_string
    return not_ab and not_cd and not_pq and not_xy

    if "ab" not in a_string and "cd" not in a_string and "pq" not in a_string and "xy" not in a_string:
        return True
    else:
        return False

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

def test_provided_examples():
    assert(check_if_string_is_nice("ugknbfddgicrmopn")) == "nice"
    assert(check_if_string_is_nice("aaa")) == "nice"
    assert(check_if_string_is_nice("jchzalrnumimnmhp")) == "naughty"
    assert(check_if_string_is_nice("haegwjzuvuyypxyu")) == "naughty"
    assert(check_if_string_is_nice("dvszwmarrgswjxmb")) == "naughty"

def test_forbidden_content():
    assert check_forbidden_content('abab') == True
    assert check_forbidden_content('abab')
    assert check_forbidden_content('acd') == False
    assert not check_forbidden_content('acd')



# def polar_coordinates_from_xy(): pass
#
# xy = polar_coordinates_from_xy()
# index = path_from_file(an_int)
#

x = 17
y = 30
class Coordinates:

    x = 10
    y = 20

    @property
    def polar(self): return self.x * 3 + self.y * 42

    @polar.setter
    def polar(self, new_polar):
        print(new_polar)



print(Coordinates().polar)
Coordinates().polar = 23

class PrimitiveCoordinates:
    polar = 42
print(PrimitiveCoordinates().polar)



# tests auch für Unterfunktionen
# auch eigene Tests schreiben
# asserts in eigene Funktion (def) - test_... muss sie dann aber heißen, damit der Testrunner sie mitnimmt
# watching_testrunner -- pytest day05_solution.py
# watching_testrunner -- pytest day05_solution.py -k test_forbidden_content