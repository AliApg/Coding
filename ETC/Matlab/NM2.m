clc
close all
clear all
%% f=@(z) z^3-0.165*z^2+3.993*10^-4;
c3=input('Enter coefficient of X^3: ');
clc
c2=input('Enter coefficient of X^2: ');
clc
c1=input('Enter coefficient of X: ');
clc
c0=input('Enter coefficient of 1: ');
clc
% a=0; b=0.11;
a=input('Enter value of "a": ');
clc
b=input('Enter value of "b": ');
clc
n=input('Enter number of repeats: ');
clc
syms z
f=@(z) c3*(z^3)+c2*(z^2)+c1*z+c0;
k=f(a); m=f(b); x=0; E=1; c=0;
while c<n
    x1=x;
    x=0.5*(a+b);
    if k*f(x)<0
        b=x;
        k=f(a);
        m=f(b);
    else
        a=x;
        k=f(a);
        m=f(b);
    end
    E=abs(x-x1)/x;
    c=c+1;
    disp([num2str(c),'.   a= ',num2str(a),'   b= ',...
        num2str(b),'   x= ',num2str(x),'   E= ',num2str(E)])
end
disp(['f (x)= ',num2str(f(x))])
ezplot(c3*(z^3)+c2*(z^2)+c1*z+c0,[-2,1]);
axis square