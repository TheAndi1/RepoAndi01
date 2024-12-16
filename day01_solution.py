from operator import index
from pathlib import Path

content = Path('day01_input.txt').read_text()
#an dieser Stelle ist nicht mal mehr die Datei offen
counter = 0
ausgabe = False


for index, zeichen in enumerate(content):
    if zeichen == "(":
        counter += 1

    elif zeichen == ")":
        counter -= 1

    if counter == -1 and ausgabe == False:
        print(index+1)
        ausgabe = True

print(counter)
