clc
clear
close all
%%
N=input('input the number of numbers: ');
I=0;M=0;
for J=linspace(1,2,N);
    A=input('input number: ');
    I=I+1;
    if A>M;
        M=A;
    end
end
disp(M)