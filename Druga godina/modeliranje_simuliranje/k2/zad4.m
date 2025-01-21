% z3.m

function y = z3(x)
    y = x .^3 - cos(3*x)


% matlab

x = -2:0.01:2;
y =  x .^3 - cos(3*x);

plot(x,y)
grid on

fzero(@z3,-1)
fzero(@z3,-0.6)
fzero(@z3,0.6)


