% clear all
% close all
% clc
% %%
% x=-5:0.1:5;
% for i=1:length(x);
%     f(i)=sin(2*x(i))/(1.5+cos(2*x(i)));
%     if x(i)>1;
%         y(i)=x(i);
%     elseif x(i)<-1;
%         y(i)=-x(i);
%     else y(i)=x(i)^2;
%     end
% end
% plot(x,f,x,y)
% axis equal
% axis square
% 
% 
% 
% %% tax
% clear all
% close all
% clc
% %%
% a=input('Enter your salary in toman: ');
% clc
% if a<=5000;
%     disp('No tax');
% elseif a>5000&&a<=100000;
%     c=0.1*(a-5000);
%     disp(['Your tax is ',num2str(c)]);
% else c=0.15*(a-100000);
%     disp(['Your tax is ',num2str(c)]);
% end


%% tax
clear all
close all
clc
%%
