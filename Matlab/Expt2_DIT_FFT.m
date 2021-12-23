% Pankaj Chaudhari
% 107
% TETA07
clc
close all
clear all

x = input("Enter the input sequence x(n): ");
N = input("Enter the length  of DFT squence:  ");
l = length(x);
if N>l
    x= [x zeros(1, N-l)];
elseif N<l
    x=x(1:N);
end
x1 = bitrevorder(x);
s = log2(N);
for p=1:s
    temp =[];
    r = 2^(s-p);
    for i = 1:r
        t = N/r;
        a = x1(t*(i-1)+1:i*t);
        l = length(a);
        temp1 = a(1:l/2);
        temp2 = a(l/2+1:l);
        k = 0:(l/2)-1;
        W = exp(-j*2*pi*r*k/N);
        temp3 = temp1+W.*temp2;
        temp4 = temp1-W.*temp2;
        temp = [temp,temp3,temp4];
    end
    x1 = temp;
end
Y = x1;
disp("DFT of the input sequence x(n) using DIT method is: ");
Y
subplot(211)
stem(Y)
x2 = input("Enter the input sequence x2(n): ");
N1 = input("Enter the length  of DFT squence:  ");
L = length(x);
if N1>L
    x2 = [x2 zeros(1,N1-L)];
elseif N1<L
    x2 = x2(1:N1);
end
w = exp(-j*2*pi/N1);
n = [0:1:(N1-1)];
k1 = [0:1:(N1-1)];
nk1 = n'*k1;
W1 = w.^nk1;
disp("N point DFT: ");
X = x2*W1;
disp("DFT of the input sequence x2(n using DFT method is :");
X
subplot(212)
stem(X)
    