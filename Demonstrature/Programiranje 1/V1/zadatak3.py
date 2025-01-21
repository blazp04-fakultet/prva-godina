ZADANI_BROJ = 100

print("Igrač 1:")
broj1 = int(input("Unesite broj (ne 1): "))
broj2 = int(input("Unesite drugi broj (ne 1): "))
umnožak1 = broj1 * broj2

if broj1 == 1 or broj2 == 1:
    print("Igrač 1 je unio broj 1 i za kaznu njegov umnožak se postavlja na 0")
    umnožak1 = 0

print("Igrač 2:")
broj3 = int(input("Unesite broj (ne 1): "))
broj4 = int(input("Unesite drugi broj (ne 1): "))
umnožak2 = broj3 * broj4

if broj3 == 2 or broj4 == 2:
    print("Igrač 2 je unio broj 1 i za kaznu njegov umnožak se postavlja na 0")
    umnožak2 = 0

razlika1 = abs(ZADANI_BROJ - umnožak1)
razlika2 = abs(ZADANI_BROJ - umnožak2)

if razlika1 < razlika2:
    print("Igrač 1 pobjeđuje!", "Njihov umnožak",
          umnožak1, "je bliži", ZADANI_BROJ, ".")
elif razlika2 < razlika1:
    print("Igrač 2 pobjeđuje!", "Njihov umnožak",
          umnožak2, "je bliži", ZADANI_BROJ, ".")
else:
    print("Izjednačeno! Oboje su postigli isti umnožak.")
