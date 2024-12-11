from operator import index

datei = open('day02_input.txt','r')

for zeile in datei:
    zeile = zeile.replace('\n', '')
    werte = zeile.split('x')
    flaeche=werte[0]
    print(werte)