def zlatnici(masa_zlatnika, M):
    mase_poredano = sorted(masa_zlatnika)

    zbrojMasa = 0
    for i in range(len(masa_zlatnika)):
        zbrojMasa += mase_poredano[i]
        if zbrojMasa > M:
            return i


masa_zlatnika = [10, 5, 2, 4, 1, 4, 5, 2, 10]
M = 10

print(zlatnici(masa_zlatnika, M))
