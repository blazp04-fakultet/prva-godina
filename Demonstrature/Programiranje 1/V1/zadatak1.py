broj1 = int(input("Unesite prvi broj: "))
broj2 = int(input("Unesite drugi broj: "))

operator = input("Unesite matematički operator (+, -, *, /, ^): ")

if operator == '+':
    rezultat = broj1 + broj2
elif operator == '-':
    rezultat = broj1 - broj2
elif operator == '*':
    rezultat = broj1 * broj2
elif operator == '/':
    print("1 - cijeli broj")
    print("2 - modul")
    print("3 - obicno djeljenje")
    opcija = int(input("Unesite odabir: "))
    if opcija == 1:
        rezultat = int(broj1 // broj2)
    elif opcija == 2:
        rezultat = broj1 % broj2
    elif opcija == 3:
        rezultat = broj1 / broj2
    else:
        rezultat = "Nepoznata opcija"
elif operator == '^':
    rezultat = broj1 ** broj2
else:
    rezultat = "Nepoznat operator"

print("Rezultat:", rezultat)
