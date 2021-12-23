clc
clear all
close all
%DSP - Expt-2 Spectral Leakage
Fx = 10;                      %Frequency of sinusoid    
Fs = 100;                     %Sampling Frequency
observationTime = 1;          %observation time in seconds
t = 0:1/Fs:observationTime;   %Time Base
x = sin(2*pi*Fx*t);           %Sampled sine wave
 
N = (256/100)*100;            %DFT length same as signal length
X1 = 1/N*fftshift(fft(x,N));  %N-point complex DFT of x
F1 = (-N/2:1:N/2-1)*Fs/N;     %frequencies on x-axis, Fs/N is the fre resolution

% N2 = (32/100)*256;          %DFT Length
X2 = 1/N*fftshift(fft(x,N));  %N-point complex DFT of x
F2 = (-N/2:1:N/2-1)*Fs/N;     %frequencies onx-axis, Fs/N is the fre resolution

figure;
subplot(3,1,1);
stem(x,'r');

title('Time Domain');
xlabel('Sample index(n)');
ylabel('x[n]');
subplot(3,1,2);              
stem(F1,abs(X1));               %Magnitude vs Frequencies
xlim([-16,16]);
title(['FFT, N=100, \Delta f=',num2str(Fs/100)]);
xlabel('f (Hz');
ylabel('|X(k)|');
subplot(3,1,3);
stem(F2,abs(X2));               %Magnitude vs Frequencies
xlim([-16,16]);
title(['FFT, N=128, \Delta f=',num2str(Fs/128)]);
xlabel('f (Hz');
ylabel('|X(k)|');