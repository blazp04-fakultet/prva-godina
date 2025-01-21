syms x
y = 3 * log(x/(x-3)) - 1
diff(y,x)

simplify(ans)
pretty(ans)

% Druga derivacija
diff(y,x,2)

simplify(ans)
pretty(ans)