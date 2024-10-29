# F. brojanje
# za dani string s i znak z rekurzivno prebroji
# koliko se puta znak pojavljuje u stringu
# npr. za 'banana' znak 'a' se pojavljuje 3 puta
def brojanje(s, z):
    if (len(s) == 1 and s[0] == z):
        return 1
    elif (len(s) == 1 and s[0] != z):
        return 0
    elif (s[0] == z):
        return 1 + brojanje(s[1:], z)
    else:
        return brojanje(s[1:], z)


print(brojanje('banana', 'a'))
