def potencija(a, b):
    if b == 0:
        return 1

    else:
        vrijednost = a*potencija(a, b-1)
        return vrijednost


print(potencija(2, 3))
