clear all
close all
clc
%%
x1=-10:0.1:10;
x2=1:0.1:10;
x3=-1:0.1:1;
x4=-10:0.1:-1;
y1=sin(2*x1)/(1.5+cos(2*x1));
y2=x2;
y3=x3.^2;
y4=-x4;
plot(x1,y1,x2,y2,x3,y3,x4,y4)
axis([-12 12 -2 12])