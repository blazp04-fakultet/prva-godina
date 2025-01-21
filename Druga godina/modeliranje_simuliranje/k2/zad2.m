% red.m

s = 0;
n = 1;
while log(n^(1/4) +1)/ exp(sqrt(n) -1) >= eps
    s = s + log(n^(1/4) +1)/ exp(sqrt(n) -1);
    n = n + 1;
end

s