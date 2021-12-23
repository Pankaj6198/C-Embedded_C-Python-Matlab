% Pankaj Chaudhari
% 107
% Root Locus

clc
close all
clear all

%% 1)
syms s;
k = 6;
n1 = 1;
d1 = sym2poly(s*(s+1));
Gs = tf(n1,d1);
Hs = 1;
figure
rlocus(Gs*Hs*k)
T = feedback(Gs*k,Hs);
figure
step(T)

%% 2)
syms s;
k = 2;
n1 = sym2poly(s+2);
d1 = sym2poly(s*(s+1));
Gs = tf(n1,d1);
Hs = 1;
figure
rlocus(Gs*Hs*k)
T = feedback(Gs*k,Hs);
figure
step(T)

%% 3)
syms s;
k = 8;
n1 = 1;
d1 = sym2poly(s*(s+1)*(s+2));
Gs = tf(n1,d1);
Hs = 1;
figure
rlocus(Gs*Hs*k)
T = feedback(Gs*k,Hs);
figure
step(T)


