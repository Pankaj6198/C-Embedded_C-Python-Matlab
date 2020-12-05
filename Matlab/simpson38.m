
% Pankaj Chaudhari
% 108
function res_simp38 = simpson38(fun,LL,UL,n)
%Simpson's 3/8th Rule: Argrument list(fun,LL,UL,n)
h=(UL-LL)/n;
s= fun(LL)+fun(UL);
for i=1:3:n-2
    s=s+ 3*(fun(LL+(i*h))+fun(LL+(i+1)*h));
end

for i=3:3:n-3
    s=s+ 2*fun(LL+(i*h));
end

res_simp38=((3*h)/8)*s;
end
