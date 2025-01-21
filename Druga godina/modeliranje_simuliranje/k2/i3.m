syms x
y = (3-x) / (2*x^2 + 2*x +1);
rez = int(y,x)

simplify(rez)
pretty(rez)