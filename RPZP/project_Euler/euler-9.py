'''
A Pythagorean triplet is a set of three natural numbers, 
, for which,

For example, 
.

There exists exactly one Pythagorean triplet for which 
.
Find the product 
.
'''


def pythagoreanTriplet():
    for a in range(1000):
        for b in range(1000):
            for c in range(1000):
                if a < b and b < c and a != 0 and b != 0 and c != 0:
                    if a**2 + b**2 == c**2:
                        if a + b + c == 1000:
                            return a*b*c


print(pythagoreanTriplet())
