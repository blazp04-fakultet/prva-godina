% Lagrangeov interpolacijski polinom

x = [-3 -1 1 3 5];
y = [3 5 6.5 -4 1];
L = polyfit(x,y,4);

k = roots(L);

x1 = -6:0.01:6;
plot(x,y,'r*',x1,polyval(L,x1));