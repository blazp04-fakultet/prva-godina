import random
import math


randomBroj = random.randint(0, 100)
print(randomBroj)


def binary_search():
    minimal = 0
    maximal = 100
    rez = maximal
    while True:
        if rez == randomBroj:
            return rez
        if rez > randomBroj:
            maximal = rez
        if rez < randomBroj:
            minimal = rez
        rez = (minimal + maximal) // 2


print(binary_search())
