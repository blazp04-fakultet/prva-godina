'''
Napiši program i funkciju loto642 koli simulira loto 6 od 42
Funkcija izvlači 6 brojeva i jedan dopusnki(gen rnd brojeva)
Funkcija vraća listu brojeva
Brojač određuje svoje brojeve, potom izvući i izračunati pogodke
'''

import random


def getRandomNumbers() -> list:
    listaBrojeva: list = []
    for i in range(6):
        broj: int = random.randint(1, 42)
        listaBrojeva.append(broj)
    dodatniBroj: int = random.randint(1, 42)
    listaBrojeva.append(dodatniBroj)
    return listaBrojeva


def enterYourNumber() -> list:
    myNumbers: list = []
    for i in range(7):
        myNumber: int = int(input("Unsite broj: "))
        myNumbers.append(myNumber)
    else:
        return myNumbers


def checNumbers(myNumber: list, allNumbers: list) -> int:
    counter: int = 0
    for number in myNumber:
        if number in allNumbers:
            counter += 1
    else:
        return counter


brojevi: list = getRandomNumbers()
mojiBrojevi: list = enterYourNumber()
pogodak: int = checNumbers(mojiBrojevi, brojevi)

print("imate", pogodak, "Točnih brojeva")
print("Izvučeni brojevi su:", brojevi)
