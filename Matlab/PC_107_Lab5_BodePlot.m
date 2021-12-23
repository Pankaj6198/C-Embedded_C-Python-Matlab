% Pankaj Chaudhari
% 107
% Root Locus

clc
close all
clear all

%% Problem Statement 1:
syms s
K = 5';
n1 = 1;
d1 = sym2poly(s*(s+3)*(s+12));
G = tf(n1,d1);
H = 1;
figure
bode(G*H*K)
T = feedback(G*K,H);
figure
step(T)

%% Problem Statement 2:
syms s
K = 30';
n1 = 1;
d1 = sym2poly(s*(s+3)*(s+12));
G = tf(n1,d1);
H = 1;
figure
bode(G*H*K)
T = feedback(G*K,H);
figure
step(T)

%% Problem Statement 3:
syms s
K = 100';
n1 = 1;
d1 = sym2poly(s*(s+3)*(s+12));
G = tf(n1,d1);
H = 1;
figure
bode(G*H*K)
T = feedback(G*K,H);
figure
step(T)


