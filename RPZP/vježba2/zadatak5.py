# D. promijesaj
# Za dane stringove a i b, vrati string koji se sastoji od a i b
# odvojenih razmakom i zamijeni prve znakove od a i b
# npr.
#   'srce', 'kuca' -> 'krce suca'
#   'tipka', 'miš' -> 'mipka tiš'
# Pretpostavka je da su a i b dulji od 1.
def promijesaj(a, b):
    a_izmjenjeni = b[0] + a[1::]
    b_izmnejeni = a[0] + b[1::]
    return a_izmjenjeni + ' ' + b_izmnejeni


print(promijesaj('srce', 'kuca'))
print(promijesaj('tipka', 'miš'))
