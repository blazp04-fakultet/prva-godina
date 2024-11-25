x1 = linspace(-4,4,100);
y1 = linspace(-4,4,100);

[x,y] = meshgrid(x1,y1);

z = tan(x.^3 .* y);

surf(x,y,z)
xlabel('x')
ylabel('y')
zlabel('z')
title('Prikaz funkcije: 1/tan(x^3*y)')