clear all
close all
clc
%%
n=input('Enter number of tosses: ');
clc
ch=0;
ct=0;
for i=1:n;
    a=round(rand);
    if a==0
        ch=ch+1;
    else ct=ct+1;
    end
end
disp(['The number of heads are ',num2str(ch),' and the number of tails are ',...
    num2str(ct)])