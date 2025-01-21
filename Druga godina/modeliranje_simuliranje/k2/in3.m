% Dvostruki integral
% D = [0,1]

% pif.m
function z = pif(x,y)
    z = sqrt(x.^2+y.^2);
 

dblquad(@pif,0,1,0,1)