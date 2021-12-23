% Pankaj Chaudhari
% 107
% IIR Filter

clc
close all
clear all

Wp = [816.8 1026.2]/3000;
Ws = [712 1130.9]/3000;
Rp = 1;
Rs = 20;
[n,wp] = cheb1ord(Wp,Ws,Rp,Rs)
[b,a] = cheby1(n,Rp,Wp);
freqz(b,a,512,60000)
title("n= 3 Chebyshev Type 1 Bandpass filter")

