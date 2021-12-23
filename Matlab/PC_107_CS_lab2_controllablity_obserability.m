% Pankaj Chaudhari
% 107
clc;
clear all;
close all;

% Controllability and Observability
A = [-1 1 0; 0 -1 0; 0 0 -2]
B = [0;4;0]
C = [1 1 1]
D = 0
Qc = ctrb(A,B)
Qo = obsv(A,C)
Qc_d = det(Qc);
Qo_d = det(Qo);
if Qc_d~=0
    fprintf("System is Controllable");
else
    fprintf("\nSystem is Uncontrollable");
end
if Qo_d~=0
    fprintf("\nSystem is Observable");
else 
    fprintf("\nSystem is Not Observable");
end
Qcl = length(A)-rank(Qc) %if other than 0 then that many states are not controllable

