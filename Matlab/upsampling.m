% Pankaj Chaudhari
% 107
% TETA07

clc
close all
clear all
% Upsampling
n = 0:10;
x = sin(2*pi*0.12*n)
y = zeros(1, 2*length(x));
y([1:2:length(y)]) = x
subplot(211)
stem(n,x)
title(' Input Sequence: ');
xlabel('Time index')
ylabel('Amplitude')
subplot(212);
stem(n,y(1:length(x)));
title('Output Sequence');
xlabel('Time index')
ylabel('Amplitude')
% clf
% n = 0:13;
% x = [1,2,3,4,5,6,7,8,8,9,9,2,1];
% y = upsample(x,2);
% subplot(211)
% stem(x);
% subplot(212)
% stem(y);




%% Down Sampling

clf
n = 0:13;
x = [1,2,3,4,5,6,7,8,8,9,9,2,1]
y = downsample(x,2);
subplot(211)
stem(x);
subplot(212)
stem(y);
