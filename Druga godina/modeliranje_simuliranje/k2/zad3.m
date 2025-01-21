% z3.m

function y = z3(x)
    y = x.^3-6.*sin(x);

% matlab

x = -3:0.01:3;
y = x.^3-6.*sin(x);

plot(x,y);

fzero(@z3,-2)
fzero(@z3,0)
fzero(@z3,2)