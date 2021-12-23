% Pankaj Chaudhari
% 107
clc
close all
clear all
x = [1 1 1 1]
L = length(x);
subplot(3,3,1)
stem(x);
title("x(n)")
for i = 2:1:9
    N = 2^i;
%     if N > L
         x = [x zeros(1,N-L)];
%     elseif N < L
%        x = x(1:N);
%     end
%     w = exp(-j*2*pi/N);
%     n = [0:1:(N-1)];
%     k = [0:1:(N-1)];
%     nk = n'*k;
%     w = w.^nk;
%     %disp("N point DFT")
%     X = w.*x;
    X = fft(x);
    a = abs(X);
    subplot(3,3,i)
    stem(X)
    title("X(k)")    
end
