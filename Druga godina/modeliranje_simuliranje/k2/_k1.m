% f.m
function y = f(x)
    a = (log(3.*x+1) - 1)./sqrt(x+1);
    b = (sin((pi.*x)./3))./sqrt(x+2);
    y = a - b;

    
x = 0:0.01:10;
a = (log(3.*x+1) - 1)./sqrt(x+1);
b = (sin((pi.*x)./3))./sqrt(x+2);

plot(x,a,x,b);

fzero(@f,2)