x1 = linspace(-2,2,100);
y1 = linspace(-2,2,100);

[x,y] = meshgrid(x1,y1);

z = sin(x.^2 + y.^2);

surf(x,y,z)
xlabel('x')
ylabel('y')
zlabel('z')
title('Prikaz funkcije: sin(x^2+y^2)')


