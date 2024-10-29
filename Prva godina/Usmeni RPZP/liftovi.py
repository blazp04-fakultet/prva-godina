
def liftovi(koraci):
    katVL = 0
    katML = 0

    presao = 0

    for kat, smjer in koraci:
        if smjer == "g":
            polaziste = 0
            odrediste = kat
        if smjer == "d":
            polaziste = kat
            odrediste = 0

        udaljenost_malog = abs(katML - polaziste)
        udaljenost_velikog = abs(katVL - polaziste)

        if udaljenost_malog <= udaljenost_velikog:
            presao += udaljenost_malog + kat
            katML = odrediste
        else:
            presao += udaljenost_velikog + kat
            katVL = odrediste

    print(presao)


koraci = [(4, "g"),
          (4, "d"),
          (3, "d")]

liftovi(koraci)
