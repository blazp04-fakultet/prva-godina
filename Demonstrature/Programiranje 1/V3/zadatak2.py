'''
 Napiši program koji od korisnika traži unos duljine 2 stranice pravokutnika.
 Ukoliko su stranice jednake, ispisati: Unijeli ste kvadrat.
 U slučaju da je unesen broj manji od 0 ispisati "Jedna stranica je manja od 0".
 Ako je prva stranica veća od druge, ispisati opseg, inače ispisati površinu tog pravokutnika.
 '''

a = int(input("Unesite prvi broj: "))
b = int(input("Unesite drugu stranicu: "))

if a == b:
    print("Unijeli ste kvadrat")

elif a < 0 or b <0:
    print("Jedna stranica je manja od 0")
elif a > b:
    o = 2*(a+b)
    print("Opseg je " + str(o))
else:
    p = a*b
    print("Povrsina je",p)
    
