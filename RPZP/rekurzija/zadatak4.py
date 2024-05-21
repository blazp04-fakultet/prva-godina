# C. palindrom
# za dani string provjeri je li palindrom
# korištenjem rekurzije (vrati True ako je palindrom)
# palindrom je string koji se čita jednako s prijeda i s traga
# npr. radar, ana, ...

def palindron(s):
    if s == "":
        return True
    if s[0] == s[-1]:
        return palindron(s[1:-1])
    else:
        return False


def polindromBezRekurzije(s):
    p = s[::-1]
    return p == s


print(palindron("ana"))
print(polindromBezRekurzije("ana"))
