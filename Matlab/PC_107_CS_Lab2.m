% Pankaj Chaudhari
% 107
clc;
clear all;
close all;

Wn = 5;
Z = 0.4;
[Num, Den] = ord2(Wn,Z);
printsys(Wn^2*Num,Den,'s');
[A,B,C,D] = ord2(Wn,Z);
A
B*Wn^2
C
D

%% given num and den
clc;
clear all;
close all;
num = 25;
den = [1 4 25]; 
wn = sqrt(den(3))
zeta = den(2)/(2*wn)
wd = wn*(sqrt(1-zeta^2))
theta = atan(sqrt(1-zeta^2)/zeta)
tr = ((pi - theta)/wd)
td = (1+ 0.7*zeta)/wn
tp = (pi/wd)
Mp = (exp(-(pi*zeta)/(sqrt(1-zeta^2))))*100
ts1 = 4/(zeta*wn)   %For 2%
ts2 = 3/(zeta*wn)   %For 5%
sys = tf(num,den)
step(sys)

