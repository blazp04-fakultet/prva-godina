# B. oba_kraja
# Za dani string s, vrati string koji se sastoji od prva 2
# i zadnja 2 znaka originalnog stringa,
# tako 'lopta' vraća 'lota'. Međutim, ako je duljina stringa
# manja od 2, vrati prazni string.
def oba_kraja(s):
    duljina = len(s)
    if (duljina < 2):
        return ''
    return s[:2] + s[-2:]


print(oba_kraja('lopta'))
print(oba_kraja('a'))
