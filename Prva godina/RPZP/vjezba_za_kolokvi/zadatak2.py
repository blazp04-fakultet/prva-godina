osobe: dict = {
    "Pero Peric": 180,
    "Mika Mikic": 190,
    "Ana Anic": 175,
    "Ivan Ivic": 165,
    "Jana Janic": 160,
    "Marko Markic": 170,
    "Jana Janic": 160,
    "Marta Bulić": 140,
    "Marko Markic": 170
}


def filtriranje(osobe: dict) -> dict:
    TRIGGER_VISINA: int = 180
    filtriraneOsobe: dict = {}
    for osoba in osobe:
        print(osoba)
        if osobe[osoba] > TRIGGER_VISINA:
            filtriraneOsobe[osoba] = osobe[osoba]
    return filtriraneOsobe


print(filtriranje(osobe))
