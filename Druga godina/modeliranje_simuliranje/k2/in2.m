% pif.m
function y=pif(x)
    y = (log(log(x)))./x

quadl(@pif,exp(1),exp(2))