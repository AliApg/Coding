clc
clear
close all
%%
tic
clc
a=0;
for b=linspace(0,1,1e5);
    a=a+1;
    %pause(1)
    disp(a)
end
t=toc