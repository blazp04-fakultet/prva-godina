
def gusari(n):
    dargulji = []
    _n = n
    for i in range(4):
        br_dragulja = _n//4
        dargulji.append(br_dragulja)
        _n -= br_dragulja

    return dargulji


print(gusari(16))
