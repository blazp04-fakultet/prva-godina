'''
Napišite program koji omogućuje korisniku da pretvori temperaturu iz Celzija u Fahrenheite ili iz Fahrenheita u Celzije. Program treba prvo pitati korisnika što želi (opcije: "C u F" ili "F u C"). Na temelju izbora, tražite unos temperature i ispišite rezultat. Koristite if za provjeru odabira.
Formula za pretvaranje iz C u F: F = C * 9/5 + 32
Formula za pretvaranje iz F u C: C = (F - 32) * 5/9

'''

print("1 - Pretvori stupnje Celzija u Fahrenheite")
print("2 - Pretvori stupnje Fahrenheita u Celzije")
temperatura = input("Unesite temperature: ")
jedinica = int(input("Unesite jedinicu (1/2): "))

if jedinica == 1:
    nova_temperatura = float(temperatura) * 9/5 + 32
    print(str(temperatura) + " stupnje Celzija je " +
          str(nova_temperatura) + " stupnje Fahrenheita")

elif jedinica == 2:
    nova_temperatura = (float(temperatura) - 32) * 5/9
    print(str(temperatura) + " stupnje Fahrenheita je " +
          str(nova_temperatura) + " stupnje Celzija")
