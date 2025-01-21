% KADA IMAMO OMEĐENO PRAVCEM
% I = dblquad(@pif, x_min, x_max, y_min, y_max)

% pif.m

function z = pif(x, y)
    z = sin(x+y);

dblquad(@pif, 0, pi/2, 0, pi)