% Pankaj Chaudhari
% 107
% TETA07
clc
close all

%read the audio signal and calculates the sampling and sampling rate
[y,Fs] = audioread("pankaj_voice.ogg"); 
t = linspace(0, length(y)/Fs, length(y));
n=length(y); % The number of points of the selection transformation point
y_p=fft (y, n); % Fourier transform, transform to the frequency domain
f=Fs*(0: n/2-1)/n; % The frequency of the corresponding point

%plotting the original audio signal in time domain
figure(1);
subplot(2,1,1);
plot(t,y);
xlabel('Time');
ylabel('Amplitude');
title('Original Audio Signal in Time Domain');

%plotting the original audio signal in frequency domain
subplot(2,1,2)
plot(f(1:n/2), y_p(1:n/2));
xlabel("Frequency"); ylabel("Amplitude");
title("Original Audio Signal in Frequency Domain");

noise=0.01*randn(n,2); % Generates random noise signals of equal length
y_z=y+noise; % The original audio signal is submerged with some random noise

%plotting the audio signal with random noise in time domain
figure(2)
subplot(2,1,1)
plot (y_z);
xlabel( 'Time');
ylabel('Amplitude A');
title("Input audio signal with added noise in Time Domain")

%Plays the audio signal with noise
sound(y_z,Fs);
pause(36);

%plotting the audio signal with random noise in frequency domain
subplot(2,1,2)
plot(f(1:n/2), y_z(1:n/2));
xlabel("Frequency"); ylabel("Amplitude");
title("Input audio signal with added noise in Frequency Domain");

%kaiser window functions
fp=1700; fc=2000; As=100; Ap=1;
wc=2*pi*fc/Fs; wp=2*pi*fp/Fs;
wdel=wc-wp;
beta=0.112*(As-8.7);
N=ceil((As-8)/2.285/wdel);
wn= kaiser (N+1, beta);
ws=(wp+wc)/2/pi;
b=fir1(N, ws, wn);
p=filter(b,1,y_z);

%Plays the filtered audio signal
sound(p,Fs);

%plotting the  Filtered audio signal
figure(3);
subplot(2,1,1);
plot(t,p);
xlabel('Time');
ylabel('Amplitude');
title('Filtered Audio signal');

%For comparing with original audio signal
subplot(2,1,2);
plot(t,y);
xlabel('Time');
ylabel('Amplitude');
title('Original Audio Signal');