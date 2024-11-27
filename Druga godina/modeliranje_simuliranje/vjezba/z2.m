x = -0.9:0.3:0.9;
y=sin(3*x);

L =polyfit(x,y,6);

x1 = -0.9:0.01:0.9;
y1 = sin(3*x1);

g1= abs(polyval(L,-0.8) - sin(3*-0.8));
g2= abs(polyval(L,0.8) - sin(3*0.8));

plot(x,y,'r*',x1,y1,x1,polyval(L,x1));