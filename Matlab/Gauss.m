clc;close all;clear all
%% Jacobi method:
n=input('Enter number of repeats: ');
Ea=input('Enter amount of error: ');
m=input('Choose method (j)acobi (g)auss seidel : ','s');
x1(1)=0;x2(1)=0;x3(1)=0;
if m=='j'
    for i=2:n
        x1(i)=1/4*(4+x2(i-1)-x3(i-1));
        x2(i)=1/6*(9-x1(i-1)-2*x3(i-1));
        x3(i)=1/5*(2+x1(i-1)+2*x2(i-1));
        E1(i)=x1(i)-x1(i-1);
        E2(i)=x2(i)-x2(i-1);
        E3(i)=x3(i)-x3(i-1);
        E=max(E1(i),E2,E3);
        if E<=Ea
            break
        end
    end
elseif m=='g'
    %% Gauss seidel method:
    for i=2:n
        x1(i)=1/4*(4+x2(i-1)-x3(i-1));
        x2(i)=1/6*(9-x1(i)-2*x3(i-1));
        x3(i)=1/5*(2+x1(i)+2*x2(i));
        E1(i)=x1(i)-x1(i-1);
        E2(i)=x2(i)-x2(i-1);
        E3(i)=x3(i)-x3(i-1);
        E=max(E1,E2,E3);
        if E<=Ea
            break
        end
    end
else
    disp('The chosen method must be j or g')
end
disp(x1,x2,x3)