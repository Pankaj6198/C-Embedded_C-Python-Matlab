
clc
close all
clear all
t= -5:0.1:5;
l=length(t);

%Unit Step
for i=1:l
    if t(i)<0
        u(i)=0;
    else
        u(i)=1;
    end
end
subplot(321);
stairs(t,u);
xlabel("t")
ylabel("u(t)")
axis([-5 5 -0.5 1.5]);
grid on;
title("Unit Step in Time Domain ");
subplot(322);
stem(t,u);
title("Unit Step in Discrete Domain ");
xlabel("n")
ylabel("u[n]")
axis([-2 2 -0.5 1.5]);
grid on;

%Unit Ramp
for i=1:l
    if t(i)<=0
        r(i)=0;
    else
        r(i)=t(i);
    end
end
subplot(323);
plot(t,r);
xlabel("t")
ylabel("r(t)")
axis([-5 5 -0.5 1.5]);
grid on;
title("Unit ramp in Time Domain ");
subplot(324);
stem(t,r);
title("Unit ramp in Discrete Domain ");
xlabel("n")
ylabel("r[n]")
axis([-2 2 -0.5 1.5]);
grid on;

%Unit Impulse
for i=1:l
    if t(i)<0  
        del(i)=0;
    elseif t(i)>0
            del(i)=0;
    else
       del(i)=1;
    end
end
subplot(325);
plot(t,del);
xlabel("t")
ylabel("del(t)")
axis([-5 5 -0.5 1.5]);
grid on;
title("Unit Impulse in Time Domain ");
subplot(326);
stem(t,del);
title("Unit Impulse in Discrete Domain ");
xlabel("n")
ylabel("del[n]")
axis([-2 2 -0.5 1.5]);
grid on;

