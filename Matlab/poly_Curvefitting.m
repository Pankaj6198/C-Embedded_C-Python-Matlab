clc;
clear all;
close all;
x=[0.4 2.5 3.3 5.0 6.2 8.0];
y=[0.7 19.3 38.2 88.2 100 115];
plot(x,y)
p=polyfit(x,y,1)
xp=0.4:.1:8.0;
yp=polyval(p,xp);
plot(x,y,"*",xp,yp)
fprintf("y= %f*x%f \n",p(1),p(2))