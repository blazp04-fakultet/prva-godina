% Prvi način
syms x
y=sqrt(atan(x))./(1+x.^2);
int(y,x,0,1)

% Drugi način

% pif.m
function y=pif(x);
    y = sqrt(atan(x))./(1+x.^2);

quadl(@pif,0,1)
