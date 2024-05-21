import math


def isPrime(n) -> bool:
    for i in range(2, round(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def sumaPrimeBrojeva():
    trigger = 2*10**6+1
    zbroj = 0
    for i in range(2, trigger):

        if isPrime(i):
            zbroj += i

    return zbroj


print(sumaPrimeBrojeva())
