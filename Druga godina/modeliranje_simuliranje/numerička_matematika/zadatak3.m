% A

P = [1 0 3 -6 0 4 0 -3];
r = roots(P)

% B

rb = [5 -4 0 3 6 -11];
pb = poly(rb)
vb = polyval(pb, [-3 6 3 1 -2])