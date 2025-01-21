'''
Ante je zaposlen u IT firmi kao developer igrica. Njegov današnji zadatak je odrediti PEGI ocjenu za novu igricu. Napišite program koji postavlja tri pitanja o sadržaju igrice (korisnik unosi "da" ili "ne"). Ako su svi odgovori "ne", igrica je PEGI-3. Ako su dva odgovora "da", igrica je PEGI-7. Ako su više od dva odgovora "da", igrica je PEGI-12.
Pitanja: 
Pojavljuli se u igrici nasilne scene
Sadrži li igrica elemente kocke ili mini igre na sreću
Prikazuje li igrica elemente konzumacije alkohola ili droge

'''

pitanje1 = input("Pojavljuli se u igrici nasilne scene (da/ne): ")
pitanje2 = input(
    "Sadrži li igrica elemente kocke ili mini igre na sreću (da/ne): ")
pitanje3 = input(
    "Prikazuje li igrica elemente konzumacije alkohola ili droge (da/ne): ")

brojac = 0

if pitanje1 == "da":
    brojac += 1
if pitanje2 == "da":
    brojac += 1
if pitanje3 == "da":
    brojac += 1

if brojac == 0:
    print("PEGI-3")
elif brojac <= 2:
    print("PEGI-7")
else:
    print("PEGI-12")
