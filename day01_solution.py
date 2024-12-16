from operator import index

with open('day01_input.txt','r') as datei: #Stichwort ContextManager, bewirkt hier, dass die Datei IMMER geschlossen wird, sobald der Context verlassen wir

    #for zeile in datei:
    #	print("Inhalt aus Datei: ")
    #	print(zeile)

    #print(datei.read())

    #print(len(datei.read()))
    counter = 0
    #position = 0
    ausgabe = False


    for index, zeichen in enumerate(datei.read()):
        #position += 1
        if zeichen == "(":
            counter += 1

        elif zeichen == ")":
            counter -= 1

        if counter == -1 and ausgabe == False:
            print(index+1)
            #print(position)
            ausgabe = True

    print(counter)
