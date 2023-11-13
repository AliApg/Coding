clc
clear all
close all
%% d=3 x=1/3
d=input('Enter amount of numerical error: ');
d=1/2*10^(-d);
clc
x=input('Enter amount of x in the equation  " e^x= 1+x/1!+...+(x^n)/n! " : ');
clc
n=0;a=0;f=1;
while  f>=d
    f=(x^(n))/factorial(n); %f=exp^x
    n=n+1;a=a+f;
end
disp(['In the equation "e^',num2str(x),'=1+',num2str(x),'/1!+...+',...
    num2str(x),'^n/n!"  n>=',num2str(n-2),' and e^',num2str(x),'=',num2str(a)])
% because the first term of the equation is called the zero term of the equation
% and at the end of while we have n+1 then at the end we have: n-1-1=n-2