% Pankaj Chaudhari
% 107
clc
close all
clear all
%% DFT
x = input("Enter input sequence");
N = input("Length of DFT N = ");
L = length(x);
if N > L
    x = [x zeros(1,N-L)];
elseif N < L
    x = x(1:N);
end
w = exp(-j*2*pi/N);
n = [0:1:(N-1)];
k = [0:1:(N-1)];
nk = n'*k;
w = w.^nk;
disp("N point DFT")
X = x*w;
subplot(1,2,1)
stem(x)
title("x(n)")
subplot(1,2,2)
stem(w)
title("X(k)")

%% IDFT
x = w %input("Enter X(k) sequence");
N = input("Length of DFT N = ");
L = length(x);
if N > L
    x = [x zeros(1,N-L)];
elseif N < L
    x = x(1:N);
end
w = exp(-j*2*pi/N);
n = [0:1:(N-1)];
k = [0:1:(N-1)];
nk = n'*k;
w = w.^(-nk);
disp("N point IDFT")
X = x*w;
subplot(1,2,1)
stem(w)
title("X(k)")
subplot(1,2,2)
stem(x)
title("x(n)")


