syms x
y = (x^2 + 3*x) / ((x+1) * (x^2 + 1))
% Prvo ide donja pa onda gornja
int(y,x,0,1)

