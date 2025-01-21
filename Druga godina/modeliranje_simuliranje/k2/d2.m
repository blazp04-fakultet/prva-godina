syms x
y = (x^3) / (1-x^3);
% Prva derivacija
diff(y,x)

simplify(ans)
pretty(ans)

% Druga derivacija
diff(y,x,2)

simplify(ans)
pretty(ans)