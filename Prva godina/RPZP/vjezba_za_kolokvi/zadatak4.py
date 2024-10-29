import random


def generiranjeListe() -> list:
    lista: list = []
    for i in range(100):
        lista.append(random.randint(0, 100))
    return lista


lista = generiranjeListe()
lista1 = lista.copy()


def sortiranje(i):
    if i % 2 == 0:
        return i
    return 0


print(lista)
print(sorted(lista1, reverse=True, key=sortiranje))
