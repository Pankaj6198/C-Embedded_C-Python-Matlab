% Pankaj Chaudhari
% 107
% FIR Filter

clc
close all
clear all

n = 26; % order
f = 60000; % Hz
fp = 254.95; % Hz
fs = 304.996; % Hz
Wp = 2*(fp/f);
Ws = 2*(fs/f);
window = kaiser(n+1);
wn = 2*(fp/f);
b = fir1(n,wn,window);
[H,w] = freqz(b,1);
subplot(211);
plot(w/pi,20*log(abs(H)));
xlabel("nf");
ylabel("Magnitude in dB");
title("Magnitude Response");
subplot(212);
plot(w/pi,angle(H));
xlabel("nf");
ylabel("Angle");
title("Phase Response");
