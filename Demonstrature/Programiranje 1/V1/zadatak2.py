godine = int(input("Unesite svoje godine: "))

if godine < 21:
    print("Ulazak zabranjen")
else:
    sati = int(input("Unesite sat: "))
    minute = int(input("Unesite minute: "))

    if (sati == 21 and minute >= 0) or (sati == 22 and minute == 0) or (sati == 22 and minute < 60):
        print("Ulazak odobren")
    else:
        print("Ulazak zabranjen")
