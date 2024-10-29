# B. parni_faktorijel
# Za dani n izračunaj umnožak svih parnih brojeva <= n
# Npr. za n = 7 dobije se 2 * 4 * 6 = 48
# Napomena: koristiti while petlju
def parni_faktorijel(n):
    umnozak = 1
    stepper = 0
    while stepper < n-1:
        stepper += 2
        umnozak = stepper * umnozak

    return umnozak


def parni_faktorijel_for(n):
    umnozak = 1
    for i in range(2, n, 2):
        umnozak *= i
    else:
        return umnozak


print(parni_faktorijel(7))
print(parni_faktorijel_for(7))
