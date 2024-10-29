def smotra(N):
    j = 0
    k = 1
    najveci_j = 1
    for i in range(1, N):
        if N % i == 0:
            k = N/i
            j = i
            if k <= j:
                break

    return (j, k)


N = 200
print(smotra(N))
