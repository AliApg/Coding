%%
clc
close all
clear all
%%
x = -pi:pi/10:pi;
y = 3*sin(x)-.5;
z = 2*cos(x);
plot(x,y,'cd:',x,z,'mo--','LineWidth',2.5,'MarkerSize',2);
xlabel('-pi < x < pi') 
ylabel('Values') 
axis image
legend('First','Second','Location','NorthOutside','Orientation','horizontal');
legend boxoff