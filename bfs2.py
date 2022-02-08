from bintreeFile import Bintree
from LinkedQFile import LinkedQ

gamla = Bintree()
svenska = Bintree()
q = LinkedQ()

with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)             # in i sökträdet


def ta_input():
    orden = list()
    orden.append(input("Ange startord: "))
    orden.append(input("Ange slutord: "))
    return orden


def makechildren(startord, slutord, q):
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
                    if nytt_ord == slutord:
                        print("Finns väg till " + slutord)
                        return True
                    else:
                        gamla.put(nytt_ord)
                        q.enqueue(nytt_ord)
        startord_lista = list(startord)
    #return q


start = "blå"
slut = "röd"
q.enqueue(start)
while not q.isEmpty():
    nod = q.dequeue()
    a = makechildren(nod, slut, q)
    if a is True:
        break
if q.isEmpty():
    print("Finns ej väg till " + slut)




