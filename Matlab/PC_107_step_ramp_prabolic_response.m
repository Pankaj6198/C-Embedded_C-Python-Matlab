
% Pankaj Chaudhari
% 107
clc;
clear all;
close all;

s = tf('s');
K = 8;
G = 13/(s*(s+3)*(s+1));
CL = G/(1+K*G);

step(CL); % step response
step(CL/s); % ramp response
step((CL/s)/s); % parabolic response
