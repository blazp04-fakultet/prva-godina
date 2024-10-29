'''
Definiraj funkciju koja kao parametar prima 2 broja te 
vraća niz brojeva djeljivih s 3 između njih.

Zatražiti od korisnike unos intervala i ispisati duljinu 
te aritmetičku sredinu niza koji smo dobili pozivom
ranije definirane funkcije.

'''

def nekaFunkcija(a,b):
    lista = []
    for i in range(a,b+1):
        if i % 3 ==0:
            lista.append(i)
    return lista

pocetak = int(input("Unesi pocetni broj: "))
kraj = int(input("Unesi krajnji broj: "))

rez = nekaFunkcija(pocetak,kraj)
duljina = len(rez)
zborj = sum(rez)
sredina = zborj/duljina
print(sredina)


