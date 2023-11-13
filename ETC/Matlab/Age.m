clc
clear
close all
%%
a=input('Input your birth year= ');
age=1398-a;
clc
if (age<2)&&(age>=0)
    disp('You are an infant')
elseif (age<=9)&&(age>=2)
  disp('You are a cild')
elseif (age<=19)&&(age>=10)
  disp('You are a teenager')
elseif (age<=29)&&(age>=20)
  disp('You are a young')
elseif (age<=49)&&(age>=30)
  disp('You are an adult')
elseif (age<=110)&&(age>=50)
  disp('You are an elderly')
else
      disp('You are dead MF : |')
end