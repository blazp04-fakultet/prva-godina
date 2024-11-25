x = -0.5:0.25:0.5;
y = exp(x);

L = polyfit(x,y,4)

% Apsolutna greška u točki x = 0.1
g1 = abs(polyval(L,0.1) - exp(0.1))

% Apsolutna greška u točki x = 1
g2 = abs(polyval(L,1) - exp(1))

% Prikaz funkcije na segmentu
x1 = -2:0.01:2;
y1 = exp(x1);
plot(x,y,'*',x1,y1,x1,polyval(L,x1));