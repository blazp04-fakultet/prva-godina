
# E. minimum
# za zadanu listu brojeva vrati najmanji broj
# korištenjem rekurzije
# npr, za [4,2,3,5] broj 2 je najmanji
def minimum(lista):
    if (len(lista) == 1):
        return lista[0]

    return min(lista[0], minimum(lista[1:]))


print(minimum([4, 2, 3, 5]))
