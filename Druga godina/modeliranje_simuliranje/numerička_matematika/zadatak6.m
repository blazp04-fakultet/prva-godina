x = -3:1:3; % Ovo je kraći način da napišem [-3 -2 -1 0 1 2 3]
y = sin(2*x);

L = polyfit(x,y,6)

% Apsolutna greška u točki x = 1
g1 = abs(polyval(L,1) - sin(2*1))

% Apsolutna vrijednost u točki x = 4
g2 = abs(polyval(L,4) - sin(2*4))

% Prikaz podataka na grafu
x1 = -3:0.01:3;
y1 = sin(2*x1);
plot(x,y,'*',x1,y1,x1,polyval(L,x1));