clear all
close all
clc
%%
n=input('Enter number of rolles: ');
clc
c1=0;c2=0;c3=0;c4=0;c5=0;c6=0;
for i=1:n;
    a=ceil(6*rand);
    if a==5
        c1=c1+1;
    elseif a==1
        c2=c2+1;
    elseif a==2
        c3=c3+1;
    elseif a==3
        c4=c4+1;
    elseif a==4
        c5=c5+1;
    else
        c6=c6+1;
    end
end
% x=(c6/n)*100;
% disp(['The possibility of sixes are ',num2str(x),' percent'])
     disp(['The number of ones are ',num2str(c1),...
    ' and the number of twos are ',num2str(c2),...
    ' and the number of threes are ',num2str(c3),...
    ' and the number of fours are ',num2str(c4),...
    ' and the number of fives are ',num2str(c5),...
    ' and the number of sixes are ',num2str(c6)])