close all
clear all
clc
%%
t = 0 : pi/50 : 2*pi;

cx1 = 5*sin(t);
cy1 = 5*cos(t);

cx2 = 5*cos(pi/4) + 5*sin(t);
cy2 = 5*cos(pi/4) + 5*cos(t);

cx3 = 10*cos(pi/4) + 5*sin(t);
cy3 = 10*cos(pi/4) + 5*cos(t);

l1 = -7.5 : 1 : 15;

l1_alternative = [0 10*cos(pi/4)];

lx2 = [-20*cos(pi/4) 20*cos(pi/4)];
ly2 = [-10*cos(pi/4) 30*cos(pi/4)];

lx2_alternative = [-5*cos(pi/4) 5*cos(pi/4)];
ly2_alternative = [5*cos(pi/4) 15*cos(pi/4)];

lx3 = [-10*cos(pi/4) 30*cos(pi/4)];
ly3 = [-20*cos(pi/4) 20*cos(pi/4)];

lx3_alternative = [5*cos(pi/4) 15*cos(pi/4)];
ly3_alternative = [-5*cos(pi/4) 5*cos(pi/4)];

plot(cx1,cy1,cx2,cy2,cx3,cy3,...
    l1,l1,l1_alternative,l1_alternative,...
    lx2,ly2,lx2_alternative,ly2_alternative,...
    lx3,ly3,lx3_alternative,ly3_alternative,...
    'linewidth',2.5)

axis equal
axis([-7 14 -7 14])