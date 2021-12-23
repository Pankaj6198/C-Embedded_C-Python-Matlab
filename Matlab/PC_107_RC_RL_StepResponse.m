clc
clear all
% RC Step Response
num = [0 1];
den = [0.0068 1];
sys = tf(num,den)
step(sys)

%% RL Step Response
clc
clear all
num = [0 1];
den = [0.0072 1];
sys = tf(num,den)
step(sys)
