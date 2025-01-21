% pif.m

function z = pif(x, y)
    z = x;

dblquad(@pif,0,3,0,4)