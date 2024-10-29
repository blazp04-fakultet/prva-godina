# B. sumparnepar
# za dani niz brojeva vrati uređeni par (x, y) gdje je x
# suma svih parnih, a y suma svih neparnih brojeva niza
# npr. za [1, 2, 3, 4, 5] se dobiva (6, 9)
# ako je niz prazan [] dobiva se (0,0)
# koristi rekurziju

def sumParNepar(niz):
    if len(niz) == 0:
        return (0, 0)
    if niz[0] % 2 == 0:
        return (niz[0] + sumParNepar(niz[1:])[0], sumParNepar(niz[1:])[1])
    else:
        return (sumParNepar(niz[1:])[0], niz[0] + sumParNepar(niz[1:])[1])


print(sumParNepar([1, 2, 3, 4, 5]))
