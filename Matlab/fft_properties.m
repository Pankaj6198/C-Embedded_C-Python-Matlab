% Pankaj Chaudhari
% 107
% TETA07
clc
close all
clear all

%% Symmetry property 
X = input("Enter the sequence: ");
y = fft(X)
z = abs(y)
if z(2)==z(8)
disp("As X(1)=X'(7), X(2)=X'(6), X(3)=X'(5)")
disp("Symmetry property is verified")
else
disp("Symmetry property is not verified")
end

%% Time Reversal
X_1= input("Enter the sequence :");
disp("The time reversed sequence is: ")
X1= [X_1(1) X_1(8) X_1(7) X_1(6) X_1(5) X_1(4) X_1(3) X_1(2)]
disp("The fft of entered sequence is: ")
y_1 = fft(X_1);
subplot(211)
stem(abs(y_1))
xlabel("DFT coefficient number")
ylabel("Angle")
title("Phase angle of a sequence")
disp("The FFT of time reversed input sequence is: ")
y1=fft(X1)
subplot(212)
stem(abs(y1))
xlabel("DFT coefficient number")
ylabel("Angle")
title("Phase angle of a sequence")
if y1 == y_1
    disp("Time reversal property is verified!")
else
    disp("Time reversal property not verified")
end

%% Linearity
x1= input("Enter the first sequence: ");
x2= input("Enter the second sequence: ");
n1= length(x1);
n2= length(x2);
if n1>n2
    k=n1-n2;
    x2= [x2 zeros(1,k)];
else
    k=n2-n1;
    x1=[x1 zeros(1,k)];
end
N= length(x1);
F1= fft(x1);
F2= fft(x2);
disp("The addition of two DSP sequence is: ")
f1= F1+F2
for i=1:N
    for j=1:N
        if(i==j)
            x(i)=x1(i)+x2(i);
        end
    end
end
x_a= fft(x)
%fprintf(x)
if(x_a==f1)
    fprintf("DFT property: Linearity Verified!")
else
    fprintf("DFT property not verified.")
end

%% Spectral Analysis
x = input("Enter the sequence: ");
l = numel(x);
subplot(2,2,1)
stem(x)
for i=2:1:l
    N = 2.^i;
    x = [x zeros(1,N-l)];
    X = fft(x)
    z = abs(X);
    subplot(2,2,i)
    stem(z)
end




