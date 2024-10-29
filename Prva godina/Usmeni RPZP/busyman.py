
import copy


def busyman(poslovi):
    p = {}

    trajanje = []
    obavljeni = 0
    for start, stop in poslovi:
        trajanje.append(stop - start)

    for _ in range(len(poslovi)):

        index_min = trajanje.index(min(trajanje))

        temp_p = copy.copy(p)
        for i in range(poslovi[index_min][0], poslovi[index_min][1]+1):
            if i in temp_p:
                trajanje.pop(index_min)
                poslovi.pop(index_min)
                break
            else:
                temp_p[i] = 1
                if i == poslovi[index_min][1]:
                    poslovi.pop(index_min)
                    trajanje.pop(index_min)
                    obavljeni += 1
                    p = copy.copy(temp_p)
                    break

    return obavljeni


poslovi = [(1, 3),
           (4, 6),
           (7, 10)]


print(busyman(poslovi))
