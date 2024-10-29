lista = [0, 1, 2, 4, 5, 6, 7, 8, 9]
my_iter = iter(lista)

while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        print('KRaj')
        break
