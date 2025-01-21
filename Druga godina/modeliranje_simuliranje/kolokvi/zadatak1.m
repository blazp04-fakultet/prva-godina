% Zadatak 2

x = 0:0.001:4;
y = log(x);
z = 2*sin(x);
q = (2*x)./(x.^2+1);

plot(x,y,x,z,x,q);
grid on


% Zadatak 3

x = -0.5:0.2:0.5;
y = cos(2*x);

L = polyfit(x,y,5);

x1 = -1:0.01:1;
y1 = cos(2*x1);

g1 = abs(polyval(L,0)-cos(2*0))
g2 = abs(polyval(L,1)-cos(2*1))

plot(x,y,'*',x1,y1,x1,polyval(L,x1));

% Zadatak 5

x1 = linspace(-2,2,100);
y1 = linspace(-2,2,100);
[x,y] = meshgrid(x1,y1);

z = sin(x).^2 + cos(y).^2;

surf(x,y,z);
title('Prikaz funkcije: sin(x)^2 + cos(y)^2');
xlabel('x');
ylabel('y');
zlabel('f(x,y)');

% Zadatak 6

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

A = [6 9 33 15;3 3 15 6;6 3 9 6;3 3 9 12];
R = [6;3;-9;-9];
x = A\R

% Zadatak 1

A = [
    sin(pi/4) -sqrt(3) -0.25;
    75^(1/3) (log10(0.8))/log(3) -exp(4);
    cos(5) tan(2*pi/3) (log(2)-0.28)
    ]

B = [
    (1/(1/tan(4))) -exp(-3) 1/tan(28);
    7^(2/3) -5/2 abs(-5+cos(pi));
    log10(4) -0.76 sin(pi/3);
    ]

C = A./B
D = C'
E = sum(D)

% Zadatak 4

(tan(3*pi/2) *(1/tan(7*pi/3)) + (2*sqrt(3))^(1/5) +asin(2/sqrt(6)) *5^(1+sqrt(3)))^(3/2) +(log(5/sqrt(4)))/exp(sqrt(4.5)) - (log10(cos(3*pi/7)))^3