

def busyman(poslovi):
    p = {}
    for start, stop in poslovi:
        for i in range(start, stop+1):
            p[i] = p.get(i, 0) + 1
    po = 0
    for posao in p:
        if p[posao] == 1:
            po += 1
    return po


poslovi = [(1, 5),
           (4, 6),
           (5, 10)]


print(busyman(poslovi))
