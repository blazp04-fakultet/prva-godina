x = [-3 -1 1 3 5 8];
y = [3 5 6.5 -4 1 -7];
L = polyfit(x,y,5)

korjeni = roots(L)

x1 = -8:0.01:8;
y1 = polyval(L,x1);

plot(x,y,'*',x1,y1)