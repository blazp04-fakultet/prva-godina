# D. glagovanje
# Za dani string
# Za dani string, ako mu je duljina barem 3,
# dodaj 'ari' na njegov kraj.
# Osim ako string već završava na 'ari', onda mu dodaj 'ti'
# Ako je duljina stringa manja od 3, ostavi ga nepromijenjenim.
# Vrati dobiveni string.
def glagovanje(s):
    if len(s) < 3:
        return
    kraj = s[-3:]
    if kraj != 'ari':
        return s + 'ari'
    return s + 'ti'


print(glagovanje('računari'))
print(glagovanje('tableti'))
