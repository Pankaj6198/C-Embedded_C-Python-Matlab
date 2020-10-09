clear all;
clc;

a=zeros(5);
for i=1:5
    for j=1:5
        if i==1
            a(i,j)=j;
            a(j,i)=j;
        elseif j<=4
                a(i,j+1)=a(i,j)+a(i-1,j+1);    
        end
    end
end


