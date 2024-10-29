
def racunanjeKoordinate(koraci):
    x, y = 0, 0

    kX = {"S": 1, "J": -1, "I": 0, "Z": 0}
    kY = {"S": 0, "J": 0, "I": 1, "Z": -1}

    for k in koraci:
        x += kX[k]
        y += kY[k]

    return (x, y)


koraci = "SSSIII"


print(racunanjeKoordinate(koraci))
