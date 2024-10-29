import random

sretniBroj: int = random.randint(0, 100)

while True:
    broj: int = int(input("Unesi Broj: "))
    if broj < 0 or broj >= 140:
        print("Broj mora biti između 0 i 140")
        continue
    if broj == sretniBroj:
        print("Svaka čast pogodio si broj :)")
        break
    else:
        print("Ae ti probaj još jednom pa možda pogodiš")

print(sretniBroj)
