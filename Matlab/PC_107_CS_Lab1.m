% Pankaj Chaudhari
% 107
clc;
clear all;
close all;

%% sys1
clc;
clear all;
close all;
%For given zeros and poles
z1=[2i -2i]';
p1=[0 0 3+4i 3-4i];
g1=1;
[num1,den1]=zp2tf(z1,p1,g1);
sys1= tf(num1,den1)

%% sys2
clc;
clear all;
close all;
%For given zeros and poles and gain
z2=[-3.2+7.8i -3.2-7.8i -4.1+5.9i -4.1-5.9i -8]';
p2=[-0.8+0.43i -0.8-0.43i -0.6];
g2=0.5;
[num2,den2]=zp2tf(z2,p2,g2);
sys2=tf(num2,den2)

%% tf2zp
clc;
clear all;
close all;
%Zeros and poles of system and transfer function
num=[3 1];             
den=[1 7 5 1 0];
sys=tf(num,den);            
[Z,P,G]=tf2zp(num,den);
num1=[7 1 63 9];
den1=[7 8 2 1 0];
sys1=tf(num1,den1)
[Z,P,G]=tf2zp(num1,den1)
