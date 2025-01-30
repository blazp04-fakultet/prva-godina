% Zadatak 1

% k1.m

function y = k1(x)
    f = (log10(3.*x+1) - 1)./sqrt(x+1);
    g = (sin((pi.*x)/3))./sqrt(x+2);
    y = f - g;

% matlab

x = 0:0.01:10;
f = (log10(3.*x+1) - 1)./sqrt(x+1);
g = (sin((pi.*x)/3))./sqrt(x+2);

plot(x,f,x,g);
grid on

fzero(@k1,3)
fzero(@k1,6)
fzero(@k1,8)

% --------------------Zadatak 2-------------------

syms x
y = 1 ./ (x.^2-5.*x+6);
int(y,x,0,1)

% k2.m
function y=k2(x)
    y = 1 ./ (x.^2-5.*x+6);

quadl(@k2,0,1)