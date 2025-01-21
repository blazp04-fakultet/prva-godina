'''
Napisati program u Pythonu koji će učitavati 10 brojeva.
 Naći i ispisati aritmetičku sredinu učitanih brojeva uzimajući u obzir samo one brojeve koji su veći ili 
jednaki 2 i manji ili jednaki 5.
'''

zbroj = 0
brojac = 0

for i in range(10):
    broj = int(input("Unesite neki broj: "))
    if broj >= 2 and broj <= 5:
        zbroj += broj
        brojac += 1

a_sredina = zbroj / brojac
print("aritmeticka sredina je",a_sredina)

