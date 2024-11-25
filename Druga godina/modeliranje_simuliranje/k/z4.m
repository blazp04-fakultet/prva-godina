x = 0:0.001:6;
y = 3.*sin(x);
z = 3.*cos(x);
q = (2*x)./sqrt(x+2);

plot(x,y,x,z,x,q);
grid on;
title('Grafovi');