% z5.m

function y = z5(x)
    f = log10(x+1);
    g = exp(x) .* sin(x);
    y = f - g;


x = -0.9:0.01:5;
f = log10(x+1);
g = exp(x) .* sin(x);

plot(x,f,x,g);
grid on

x = -0.9:0.01:0.5;
f = log10(x+1);
g = exp(x) .* sin(x);

plot(x,f,x,g);
grid on

fzero(@z5,-0.6)
fzero(@z5,0)
fzero(@z5,3)