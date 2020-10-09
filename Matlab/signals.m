clc;
clear;
close all;

t=-5:0.01:5; 

%Unit Step
unit_step=[t>=0];
subplot(3,2,1)
plot(t,unit_step,"r","Linewidth",2)
xlabel("t");
ylabel("u(t)");
title("Unit Step Signal in Continous Domain ");

subplot(3,2,2)
stem(t,unit_step,"r");
xlabel("n");
ylabel("u[n]");
title("Unit Step Signal in Discrete Domain ");

%Unit Ramp 
unit_ramp=t.*[t>=0];
subplot(3,2,3)
plot(t,unit_ramp,"g","Linewidth",2)
xlabel("t");
ylabel("r(t)");
title("Unit Ramp Signal in Continous Domain ");

subplot(3,2,4)
stem(t,unit_ramp,"g");
xlabel("n");
ylabel("r[n]");
title("Unit Ramp Signal in Discrete Domain ");

%Unit Impulse signal
unit_impulse=[t==0];
subplot(3,2,5)
plot(t,unit_impulse,"b","Linewidth",2)
xlabel("t");
ylabel("delta(t)");
title("Unit Impulse Signal in Continous Domain ");

subplot(3,2,6)
stem(t,unit_impulse,"b");
xlabel("n");
ylabel("delta[n]");
title("Unit Impulse Signal in Discrete Domain ");




