# E. parne_znamenke
# za dani prirodni broj n vrati broj koji je
# nastao od broja n kojemu su izbačene neparne
# znamenke.
# ako n nema parnih znamenki onda vrati 0
# npr. za 1234 vrati 24
def parne_znamenke(n):
    s = "0"
    str_n = str(n)
    for b in str_n:
        if int(b) % 2 == 0:
            s += b
    else:
        return int(s)


print(parne_znamenke(1234))
