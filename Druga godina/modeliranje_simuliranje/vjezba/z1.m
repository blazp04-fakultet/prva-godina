x = -0.5:0.2:0.5;
y = cos(2*x);

L = polyfit(x,y,5)

x1 = -0.5:0.01:0.5;
y1 = cos(2*x1);

g1 = abs(polyval(L,0) - cos(2*0))
g2 = abs(polyval(L,1) - cos(2*1))

plot(x,y,'*',x1,y1,x1,polyval(L,x1));