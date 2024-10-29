lista = [0, 1, 2, 4, 5, 6, 7, 8, 9]
my_iter = iter(lista)

print(lista)
print(my_iter)

'''
# Lista svih metda u iteraciji
for el in dir(my_iter):
    print(el)
'''

# ide sljedeći element u listi
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# isto je koristili iter ili listu
for broj in my_iter:
    print(broj)
