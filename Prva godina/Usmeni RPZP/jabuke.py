
def jabuke(N, K, S):
    for i in range(S):
        if provjera(i, N, K, S):
            return i


def provjera(X, N, K, S):
    rez = 0
    for i in range(N):
        rez += X+(i*K)
    return rez == S


N, K, S = 5, 2, 45
print(jabuke(N, K, S))
