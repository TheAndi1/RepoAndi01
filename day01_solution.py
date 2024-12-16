from operator import index
from pathlib import Path
import sys

content = Path('day01_input.txt').read_text()
#an dieser Stelle ist nicht mal mehr die Datei offen

mapping = {
    "(" : +1,
    ")": -1,
}
counter = 0
ausgabe = False
for index, zeichen in enumerate(content):

    counter += mapping[zeichen]

    if counter == -1 and ausgabe == False:
        print(index+1)
        ausgabe = True

print(counter)
