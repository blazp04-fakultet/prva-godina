'''
Korištenjem while petlje i break izkaza od korisnika 
tražiti unos brojeva u niz sve dok ne unese “x” ili
“X” . Unesene brojeve dinamički spremati u niz.


Napisati funkciju koja kao argument prima niz i 
računa prosjek samo parnih brojeva.
Funkcija kao rezultat vraća taj prosjek u glavni program.

'''

niz = []
while True:
    broj = input("Unesi broj: ")
    if broj.lower() == "x":
        break
    else:
        niz.append(int(broj))


def prosjek(niz):
    lista = []
    for i in niz:
        if i % 2 == 0:
            lista.append(i)
    pros = sum(lista)/len(lista)
    return pros


rez = prosjek(niz)

print("Prosjek brojeva je", rez)
