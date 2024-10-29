def zabava(ljudi):
    sekunde = {}
    for a, b in ljudi:
        for i in range(a, b+1):
            sekunde[i] = sekunde.get(i, 0) + 1
    return max(sekunde, key=sekunde.get)


ljudi = [(1, 3), (2, 3), (3, 4), (5, 7)]
print(zabava(ljudi))
