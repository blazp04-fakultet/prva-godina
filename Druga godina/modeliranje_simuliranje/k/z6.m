x = -3:1:3;
y = sin(2*x);

L = polyfit(x,y,6)

x1 = -3:0.01:3;
y1 = sin(2*x1);
plot(x,y,'*',x1,y1,x1,polyval(L,x1));


