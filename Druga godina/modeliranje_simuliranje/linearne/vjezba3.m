% Carmeov
A = [6 9 33 15;3 3 15 6;6 3 9 6;3 3 9 12];
d = det(A);
A1 = [6 9 33 15;3 3 15 6;-9 3 9 6;-9 3 9 12];
d1 = det(A1);
A2 = [6 6 33 15;3 3 15 6;6 -9 9 6;3 -9 9 12];
d2 = det(A2);
A3 = [6 9 6 15;3 3 3 6;6 3 -9 6;3 3 -9 12];
d3 = det(A3);
A4 = [6 9 33 6;3 3 15 3;6 3 9 -9;3 3 9 -9];
d4 = det(A4);

x1 = d1/d
x2 = d2/d
x3 = d3/d
x4 = d4/d

% matrični

B = [6 9 33 15;3 3 15 6;6 3 9 6;3 3 9 12];
R = [6;3;-9;-9];

x = B\R
