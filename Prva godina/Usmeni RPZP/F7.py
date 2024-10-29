def F7(bodovi):
    broj_trkaca = len(bodovi)
    teoretskiu_maximum_bodova = []
    teoretskiu_minimum_bodova = []
    moguci_pobjednici = 0

    for trkac in bodovi:
        teoretskiu_maximum_bodova.append(trkac+broj_trkaca)
        teoretskiu_minimum_bodova.append(trkac+1)

    for i in range(broj_trkaca):
        max_bodovi = teoretskiu_maximum_bodova[i]
        for j in range(broj_trkaca):
            if i == j:
                continue
            min_bodovi = max(teoretskiu_minimum_bodova)
            if min_bodovi <= max_bodovi:
                moguci_pobjednici += 1
                break

    return moguci_pobjednici


bodovi = [15, 13, 16, 9, 10, 12]
print(F7(bodovi))
