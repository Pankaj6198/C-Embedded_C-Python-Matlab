clc
clear all
close all

syms w t z n a; 
% Fourier Transform
 disp("Fourier Transform")
 %syms w t n a;    %Symbols
 x= a*sin(t)
 y= fourier(x)  %LT
 z=ifourier(y)  % Inverse LT
 simplify(y)    % gives Simplified eqn 
 pretty(y)      % Given Most readable form 
 


% Laplace Transform
disp("Laplace Transform") 
% syms s t a;    %Symbols
 x= a*sin(t)
 y= laplace(x)  %LT
 z=ilaplace(y)  % Inverse LT
 simplify(y)    % gives Simplified eqn 
 pretty(y)      % Given Most readable form 
 
 
 % Z Transform
 disp("Z Transform")
 syms z n a;     
% x= sin(t)
 y=ztrans(x)      % ZT
 z=iztrans(y)     %Inverse ZT