import random


def sortiranje(lista):

    duljiva = len(lista)

    for i in range(duljiva):
        for j in range(0, duljiva-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista


def generiranjeRandomNiza():

    lista = []
    for i in range(100):
        lista.append(random.randint(0, 1000))

    return lista


print(sortiranje(generiranjeRandomNiza()))
