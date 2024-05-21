def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fiboNizBezrekurzije(n):
    rez = []
    for i in range(n):
        if i == 0:
            rez.append(0)
        elif i == 1:
            rez.append(1)
        else:
            rez.append(rez[i - 1] + rez[i - 2])
    else:
        return rez[-1]+rez[-2]


t = 4000
# print(fib(t))
print(fiboNizBezrekurzije(t))
