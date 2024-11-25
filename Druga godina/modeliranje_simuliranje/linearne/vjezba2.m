% Carmen
A = [0 -6 3;-2 1 -1;3 -2 0];
A1 = [7 -6 3;-3 1 -1;2 -2 0];
A2 = [0 7 3;-2 -3 -1;3 2 0];
A3 = [0 -6 7;-2 1 -3;3 -2 2];

d = det(A);
d1 = det(A1);
d2 = det(A2);
d3 = det(A3);

x1 = d1/d
x2 = d2/d
x3 = d3/d

% Matrični način
B = [0 -6 3;-2 1 -1;3 -2 0];
R = [7;-3;2];

x = B\R
