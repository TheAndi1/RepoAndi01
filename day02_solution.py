# https://adventofcode.com/2015/day/2

from operator import index
from pathlib import Path

content = Path('day02_input.txt').read_text()

def area_and_ribbon_length_for_present_of_size(line):
    werte = line.split('x') #mittels der SPLIT Funktion die drei Werte in eine Liste übertragen, Zeile für Zeile

    #GeschenkpapierBerechnung
    flaeche = (2 * (int(werte[0]) * int(werte[1]))) + (2 * (int(werte[0]) * int(werte[2]))) + (2 * (int(werte[1]) * int(werte[2])))
    zusatz = min((int(werte[0]) * int(werte[1])), (int(werte[0]) * int(werte[2])), (int(werte[1]) * int(werte[2])))

    #GeschenkbandBerechnung
    kleinste = min(int(werte[0]), int(werte[1]), int(werte[2]))
    mitte = int(werte[0]) + int(werte[1]) + int(werte[2]) - min(int(werte[0]), int(werte[1]), int(werte[2])) - max(int(werte[0]), int(werte[1]), int(werte[2]))
    groesste = max(int(werte[0]), int(werte[1]), int(werte[2]))

    band = kleinste + kleinste + mitte + mitte
    schleife = kleinste * mitte * groesste

    #finale Berechnungen
    return flaeche + zusatz, band + schleife

gesamtflaeche = 0
gesamtband = 0

for zeile in content.splitlines():
    zeile = zeile.replace('\n', '') #in jeder Zeile \n (Zeilenumbruch rausschmeißen)

    area, ribbon_length = area_and_ribbon_length_for_present_of_size(zeile)
    gesamtflaeche = gesamtflaeche + area
    gesamtband = gesamtband + ribbon_length


print(gesamtflaeche) #Part One der Aufgabe
print(gesamtband) #Part Two der Aufgabe

assert gesamtflaeche == 1606483
assert gesamtband == 3842356

#wir benutzen die Beispiele als TestCases und rufen die Funktion auf und vergleichen die Rückgabewerte mit dem erwarteten Ergebnis
# "testgetriebene Entwicklug"
assert area_and_ribbon_length_for_present_of_size('2x3x4') == (58, 34)
assert area_and_ribbon_length_for_present_of_size('1x1x10') == (43, 14)