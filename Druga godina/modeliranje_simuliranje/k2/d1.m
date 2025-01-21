syms x
y = log(sqrt(((x-1)^3)/(x+1)))

% Određivanje prve derivacije funkcije
diff(y,x)

simplify(ans)
pretty(ans)

% Određivanje druge derivacije funkcije
diff(y,x,2)

simplify(ans)
pretty(ans)