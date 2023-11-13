clear all
close all
clc
%%
while 0==0
    a=input('Enter a chatacter: ','s');
    clc
    if a>=65&&a<=90
        disp([(a),' is captal'])
    elseif a>=97&&a<=122
        disp([(a),' is small'])
    else
        disp('Character is wrong')
    end
end