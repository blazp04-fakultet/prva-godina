import random


def generiranjeListe() -> list:
    lista: list = []
    for i in range(100):
        lista.append(random.randint(0, 100))
    return lista


def prebrojavanjeListe(listaBrohjave: list) -> dict:
    brojevi: dict = {}
    for broj in listaBrohjave:
        if broj in brojevi:
            brojevi[broj] += 1
        else:
            brojevi[broj] = 1
    return brojevi


def brojeviKojiSePojavljujuViseOdTriPuta(brojevi: dict) -> dict:
    finalniBrojevi: dict = {}
    for broj in brojevi:
        if brojevi[broj] > 3:
            finalniBrojevi[broj] = brojevi[broj]

    return finalniBrojevi


listaBrjeva: list = generiranjeListe()
brojPonavljanjaBrojeva: dict = prebrojavanjeListe(listaBrjeva)
finalniBrojevi = brojeviKojiSePojavljujuViseOdTriPuta(brojPonavljanjaBrojeva)
print(finalniBrojevi)
