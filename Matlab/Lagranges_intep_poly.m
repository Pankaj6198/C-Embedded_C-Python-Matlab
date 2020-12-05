clc;
clear all;
close all;
% Pankaj Chaudhari
% 108
syms x;
S=0;
X=[5 7 11 13 17];
[r,n]=size(X);
Y=[150 392 1452 2366 5202];

for i=1:n
    L=1;
    for j=1:n
        if j~=i
            L=L*(x-X(j))/(X(i)-X(j));
        end
    end
    S=S+Y(i)*L;
end

fprintf("y(x)=%s",expand(S))        
p=polyfit(X,Y,3);
xp=5:.1:17;
yp=polyval(p,xp);
plot(X,Y,"--",xp,yp)
fprintf("\nf(9)= %.1f\n",polyval(p,9))

