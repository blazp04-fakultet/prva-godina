# lProgram koji rekurzijom radi zbroj brojeva

def zbroj(n):
    if n == 0:
        return 0
    z = n + zbroj(n - 1)
    return z


print(zbroj(100))
