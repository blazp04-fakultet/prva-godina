def skoroNajveci(lista):
    sortirana = sorted(lista)

    najveci = sortirana[-1]
    for i in range(1, len(sortirana)):
        if sortirana[-i] != najveci:
            return sortirana[-i]
    return "-"


ulaz = [9, 9, 9, 9]


print(skoroNajveci(ulaz))
