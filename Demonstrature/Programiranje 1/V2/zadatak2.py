'''
Napišite program koji pomaže korisniku izračunati napojnicu u restoranu. Program prvo treba pitati korisnika za iznos računa, a zatim za postotak napojnice (npr. 10%, 15%, 20%). Na temelju unosa, program treba izračunati iznos napojnice i ukupni iznos za plaćanje.
Finalna cijena se računa prema formuli: cijena * (1+(napojnica/100))
'''

iznos = float(input("Unesite iznos računa: "))
napojnica = int(input("Unesite postotak napojnice: "))

finalna_cijena = iznos * (1 + (napojnica/100))

print("Iznos sa napojnicom je: " + str(finalna_cijena))
