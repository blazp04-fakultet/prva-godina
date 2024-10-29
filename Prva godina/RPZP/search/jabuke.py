"""
Ivica slavi rođendan i pozvao je N prijatelja. Svaki prijatelj mu je na 
dar donio jabuke i to:
1. prijatelj – X jabuka 
2. prijatelj – K jabuka više od 1. prijatelja
3. prijatelj – K jabuka više od 2. prijatelja
… 
N. prijatelj – K jabuka više od (N-1). prijatelja

Ako je Ivica ukupno dobio S jabuka, odredite koliko jabuka mu je 
donio prvi prijatelj.
"""

# n - broj prijatelja
# k - povećanje
# s - zbroj


def provjera(n, k, s):
    zbroj = 0
    zadnji = 1
    for i in range(1, n+1):
        zbroj += zadnji
        zadnji = zadnji + k
    return zbroj - s


def pogodiK(n, s):
    minimalno = 0
    maximalno = s
    k = maximalno
    while True:
        rez = provjera(n, k, s)
        if rez == 0:
            return k
        if rez > 0:
            maximalno = k
        if rez < 0:
            minimalno = k
        k = (minimalno + maximalno) // 2


# print(provjera(5, 2, 25))

print(pogodiK(5, 25))
