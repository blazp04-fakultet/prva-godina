'''
Postavite parametre kružnice polumjer r  i koordinate središta (a,b)
Zatim je potrebno učitati 10 točaka koordinatnog sustava
Za učitane točke provjeriti da li se nalaze na kružnici
Ispisati broj točaka na kružnici i omjer
(x-a)**2 + (y-b)**2 = r**2
'''

a = 1
b = 5
r = 10

tocke = [
    [3, 5],
    [1, 2],
    [9, 8],
    [1, 8],
    [4, 8],
    [3, 6],
    [1, 9],
    [9, 6],
    [1, 4],
    [4, 2],
]

tockeUKruznici = []
promjer = r**2
for tocka in tocke:
    rez = (tocka[0] - a) ** 2 + (tocka[1] - b) ** 2
    if rez <= promjer:
        tockeUKruznici.append(tocka)
else:
    print("tocke koje se nalaze u kruznici su:", tockeUKruznici)
