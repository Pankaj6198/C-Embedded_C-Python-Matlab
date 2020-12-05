% Pankaj Chaudhari
% 108
% Newton's Forward Interpolation 
clc;
clear all;
x1= input("Enter Starting Value of x ");
x2= input("Enter Last Value of x ");
h= input("Enter Interval ");
x=x1:h:x2;
[row,n]=size(x); % n= no. of points
disp("Enter corresponding values of y");
for i=1:n
    y(i,1)=input(" ");
end
yy=y';
% forward difference table
for j=2:n
    for i=1:n-j+1
    y(i,j)=y(i+1,j-1)-y(i,j-1);
    end
end
fprintf("\n  forward difference table \n");
fprintf("\n\t   x\t      y\t    del1y\tdel2y\tdel3y\tdel4y ");
for i=1:n
    fprintf("\n %  .f",x(i));
    for j=1:n-i+1
        fprintf("\t  % .f",y(i,j));
    end
end

% Newtons forward difference formula

req_x =input("\n Enter x for which y is to be calculated ");
u= (req_x - x(1))/h ;
res=y(1);

for i=1:n-1
term=1;
    for j=1:i
        % Finding values of u terms
        term=term*(u-j+1)/j;
    end
    %summing up the terms
    res=res + term * y(1,i+1);
end
fprintf("\n(From Newtons interpolation) f(%.2f) = %.4f",req_x,res);

% Interpolating polynomial
 p=polyfit(x,yy,3)
 xp=0:0.1:5;
 yp=polyval(p,xp);
 plot(x,yy,"--",xp,yp)
 fprintf("y= %.fx^3%.fx^2%.fx+%.f \n",p(1),p(2),p(3),p(4))
 fprintf("(Using Interpolating polynomial  ) f(0.5)= %.4f \n",polyval(p,0.5))


    
        