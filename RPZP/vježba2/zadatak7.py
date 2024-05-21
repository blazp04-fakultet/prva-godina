
# F. pred_zad
# Dijeljenje stringa na dva dijela.
# Ako je duljina stringa parna, prednja i zadnja polovica su iste duljine
# Ako je duljina stringa neparna, neka prednja polovica ima znak više
# npr. 'abcde', prednja polovica je 'abc', a zadnja 'ef'
# Za dana 2 stringa, a and b, vrati string oblika
#  prednje od a + prednje od b + zadnje od a + zadnje od b
import math


def pred_zad(a, b):
    duljina_a = len(a)
    prva_polovica_a = math.ceil(duljina_a / 2)

    duljina_b = len(b)
    prva_polovica_b = math.ceil(duljina_b / 2)

    rez = a[:prva_polovica_a] + b[:prva_polovica_b] + \
        a[prva_polovica_a:] + b[prva_polovica_b:]

    return rez


print(pred_zad('abcde', "1234"))
