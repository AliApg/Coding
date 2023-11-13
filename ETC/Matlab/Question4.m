close all
clear all
clc
%%
n = 1;
while n ~= 21
    
    x = input(['Enter number ',num2str(n),': '],'s');

    try %Solve
        x = num2str(eval(x));
    catch
    end
    
    n = n+1;
    
    if isnan(str2double(x)) %%Not a number
        
        n = n-1;
        clc
        fprintf('Plese only enter numeric inputs!\n\n')
        
    elseif str2double(x) == 0 %%Zero
        
        clc
        fprintf('Input is "Zero"\n\n')
        
    elseif mod(str2double(x),2) == 0 %%Even
        
        clc
        fprintf([x,' is "Even"\n\n'])
        
    else %%Odd
        
        clc
        fprintf([x,' is "Odd"\n\n'])
        
    end
    
end