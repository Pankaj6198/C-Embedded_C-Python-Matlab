%%   Driver Code
% Pankaj Chaudhari
% 108
clc;
clear all;

fun=@(x) (log(x));
a=input("Enter Lower Limit : ");
b=input("Enter Upper Limit: ");
n=input("Enter no. of sub-interval: ");

fprintf("\nI(By Trapizoidal Rule)= %f \n",trap(fun,a,b,n))
while rem(n,3)~=0
     disp("n must be multiple of 3 for Simpson's 3/8th Rule ")
     n=input("Enter no. of sub-interval: \n");
 end
 fprintf("I(By Simpson's 3/8th Rule)= %f \n\n",simpson38(fun,a,b,n))
 
 while rem(n,2)~=0
     disp("n must be even for Simpson's 1/3th Rule")
     n=input("Enter no. of sub-interval: \n");
 end
 fprintf("I(By Simpson's 1/3th Rule)= %f \n",simpson13(fun,a,b,n))

 disp("Using int() function :")
 f=inline("log(x)","x");
 syms x;
 fprintf("I(By int() function )= %f \n",int(f(x),a,b))



