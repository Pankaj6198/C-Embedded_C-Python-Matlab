
% Pankaj Chaudhari
% 108

function res_trap = trap(fun,LL,UL,n)
%Trapiziodal Rule: Argrument list(fun,LL,UL,n)
h=(UL-LL)/n;
s=0.5*(fun(LL)+fun(UL));

for i=1:n-1
    s=s+fun(LL+(i*h));
end
res_trap=h*s;
end
