from operator import index


datei = None
try: #leitet ExceptionListening ein
    datei = open('day02_input.txt','r')
    gesamtflaeche = 0
    gesamtband = 0

    for zeile in datei:
        zeile = zeile.replace('\n', '') #in jeder Zeile \n (Zeilenumbruch rausschmeißen)
        werte = zeile.split('x') #mittels der SPLIT Funktion die drei Werte in eine Liste übertragen, Zeile für Zeile

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
        gesamtflaeche = gesamtflaeche + flaeche + zusatz
        gesamtband = gesamtband + band + schleife

    print(gesamtflaeche) #Part One der Aufgabe
    print(gesamtband) #Part Two der Aufgabe

finally: #auch bei Exceptions kommt er hier vorbei
    datei.close()