clc
clear all
close all
% Genration of Sine wave
% Q1: a)
 t=0:0.01:1;
 f1=1080; % Roll no: 108 * 10 
 sin_wave1= sin(2*pi*f1*t);
 subplot(4,2,1)
 plot(t,sin_wave1)
 title("Continous Time Domain")
 xlabel("t")
 ylabel("x(t)")
 subplot(4,2,2)
 stem(t,sin_wave1)
 title("Discrete Time Domain")
 xlabel("n")
 ylabel("x(t)")
 % b)
 f2=2160; % Roll no: 108 * 20
 sin_wave2= sin(2*pi*f2*t);
 subplot(4,2,3)
 plot(t,sin_wave2)
 xlabel("t")
 ylabel("x(t)")
 subplot(4,2,4)
 stem(t,sin_wave2)
 xlabel("n")
 ylabel("x(t)")
 
 % c)
 final_signal= sin_wave1 + sin_wave2;
 subplot(4,2,5)
 plot(t,final_signal)
 title("Combined Signal")
 xlabel("t")
 ylabel("x(t)")
 subplot(4,2,6)
 stem(t,final_signal)
 xlabel("n")
 ylabel("x(t)")
 
 %d)
 t=t+200;
 subplot(4,2,7)
 plot(t,final_signal)
 title("Delayed by 200")
 xlabel("t")
 ylabel("x(t)")
 subplot(4,2,8)
 stem(t,final_signal)
 xlabel("n")
 ylabel("x(t)")
 
 
 
 
 