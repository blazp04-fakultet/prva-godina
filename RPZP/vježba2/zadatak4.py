# C. fiksni_start
# Za dani string s, vrati string
# u kojem su svi znakovi koji su jednaki prvom znaku
# promijenjeni u '*', osim prvog znaka
# npr. 'anatomija' vraća 'an*tomij*'

def fiksni_start(s):
    rijec = ''
    prvi = ''
    for slovo in s:
        if slovo == prvi:
            rijec += '*'
        else:
            rijec += slovo
            if prvi == '':
                prvi = s[0]
    return rijec


print(fiksni_start('anatomija'))
