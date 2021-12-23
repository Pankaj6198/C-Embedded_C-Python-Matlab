clc
clear all
close all

syms s

t1 = 0:0.1:50;
u1 = t1;
num = 25;
den = [1 4 25];
sys = tf(num,den);
figure
step(sys)
[y,t,x] = lsim(sys,u1,t1);
figure
plot(t,y,t,u1)
title("Ramp Response")
t2 = 0:0.1:20;
u2 = 0.5*t2.*t2;
[y,x] = lsim(sys,u2,t2);
figure
plot(t2,y,t2,u2)
title("Parabolic Response")
