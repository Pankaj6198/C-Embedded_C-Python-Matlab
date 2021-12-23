% Pankaj Chaudhari
% 107
clear all; 
clc; 

% Butterworth using Bilinear 
wp=input('Enter passband edge frequency: ');
wc=input('Enter stopband edge frequency: '); 
rp=input('Enter passband attenuation: '); 
rs=input('Enter stopband attenuation: '); 
fs=input('Enter sampling frequency: '); % calculate order and cutoff frequency  
[n,wn]=buttord(wp,wc,rp,rs,'s'); 
% calculate numerator and denominator coefficients H(s) 
[b,a]=butter(n,wn,'s'); 
% Using Bilinear Transformation H(z) 
[num,den]=bilinear(b,a,fs); 
% Frequency response 
freqs(b,a); 
title("Butterworth using Bilinear transformation") 
figure; 
% Using Impulse Invariance 
% calculate order and cutoff frequency 
[n,wn]=buttord(wp,wc,rp,rs,'s'); 
% calculate numerator and denominator coefficients H(s)  
[b,a]=butter(n,wn,'s'); 
% Using impulse invariance Transformation H(z) 
[num,den]=impinvar(b,a,fs); 
% Frequency response 
freqs(b,a) 
title("Butterworth using Impulse Invariance ")
