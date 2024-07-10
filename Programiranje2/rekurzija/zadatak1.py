def faktorijel(n):
    # Bazni slučaj
    if n == 1:  # ili n == 0
        return 1

    # Rekurzivni slučaj: n! = n * (n-1)!
    else:
        return n * faktorijel(n-1)


print(faktorijel(5))


