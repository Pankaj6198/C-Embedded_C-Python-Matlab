
% Pankaj Chaudhari
% 108
function res_simp13 = simpson13(fun,LL,UL,n)
%Simpson's 1/3th Rule: Argrument list(fun,LL,UL,n)
h=(UL-LL)/n;
s= fun(LL)+fun(UL);
for i=1:2:n-1
    s=s+ 4*fun(LL+(i*h));
end

for i=2:2:n-2
    s=s+2*fun(LL+(i*h));
end

res_simp13=(h/3)*s;

end



