A = [cos(pi/3) -sqrt(3) 9.78;(1-6.2^(1/3)) log10(0.8) (-exp(4));1.5 tan(2*pi/3) 0.34]
B = [1/atan(4) -exp(-2) 1/tan(15);sqrt(6) (-5/2) -1; 0.24 -0.55 sin(pi)]

C = A .* B
D = C'
E = sum(D)