clear all
close all
clc
%%
a=input('enter a number: ');
max=a;min=a;z='end';
while a~=z
    if a>=max
        max=a;
    elseif a<=min
        min=a;
    end
    a=input('enter a number: ');
    clc
end
disp([num2str(max),' is maximum value and ',...
    num2str(min),' is minimum value'])