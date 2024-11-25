x = -6:2:6;
y = cos(4*x);
L = polyfit(x,y,6)

g1 = abs(polyval(L,-7) - cos(4*-7))
g2 = abs(polyval(L,5) - cos(4*5))

x1 = -6:0.01:6;
y1 = cos(4*x1);
plot(x,y,'*',x1,y1,x1,polyval(L,x1));