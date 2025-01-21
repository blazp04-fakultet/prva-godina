% suma.m
s = 0;
n = 1;
while (n+1)/(n^4) >= eps
    s = s + (n+1)/(n^4);
    n = n + 1;
end

s