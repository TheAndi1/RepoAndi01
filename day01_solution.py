from operator import index

datei = None
try: #leitet ExceptionListening ein
    datei = open('day01_input.txt','r')

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
except FileNotFoundError as e:
    print('You moron, give the right file')
finally: #auch bei Exceptions kommt er hier vorbei
    datei.close()
