# Po naški dictionary

rijecnik = dict()  # ili samo {}

rijecnik['ja'] = "nisam"
rijecnik['ti'] = "nisi"
rijecnik['on'] = "nije"

osoba = {
    'ime': 'Pero',
    'prezime': 'Peric',
    'godine': 30
}

del osoba['godine']

for key in osoba:
    print(key, osoba[key])

print(rijecnik)
print(osoba)


# provjeravanje postoji li ključ

if 'prebivaliste' in osoba:
    print('prebivaliste postoji')
