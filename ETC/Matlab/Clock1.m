clear all
close all
clc
%%
t=0:pi/30:2*pi;
x=10*sin(t);
y=10*cos(t);
T1=0;T2=0;
%   for T2=0:pi/6:2*pi;
%     for T1=0:pi/30:2*pi;
while 0==0;
    for T=0:pi/30:2*pi;
        T1=T1+(pi/30)*(1/60);
        T2=T2+(pi/30)*(1/60)*(1/12);
        x1=9.5*sin(T);
        y1=9.5*cos(T);
        x2=8.15*sin(T1);
        y2=8.15*cos(T1);
        x3=7*sin(T2);
        y3=7*cos(T2);
        plot(x,y,[0,x1],[0,y1],[0,x2],[0,y2],[0,x3],[0,y3])
        axis equal
        axis([-12 12 -12 12])
        pause(1);
    end
end
% end
% end