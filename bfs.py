from bintreeFile import Bintree

svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)             # in i sökträdet

gamla = Bintree()

def ta_input():
    orden = list()
    orden.append(input("Ange startord: "))
    orden.append(input("Ange slutord: "))
    return orden


def makechildren(startord):
    gamla.put(startord)
    startord_lista = list(startord)
    bokstaver = "abcdefghijklmnopqrstuvwxyzåäö"
    for bokstav_position in range(len(startord_lista)):
        for bokstaven in bokstaver:
            startord_lista[bokstav_position] = bokstaven
            nytt_ord = "".join(startord_lista)
            if nytt_ord in gamla:
                pass
            else:
                if nytt_ord in svenska:
                    gamla.put(nytt_ord)
                    print(nytt_ord)
        startord_lista = list(startord)

makechildren("ute")

