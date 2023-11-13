clc
clear
close all
%%
b=input('Input Your Madrak ( b or m or p ): ','s');
clc
if b=='b';
    const=10;
elseif b=='m';
    const=12;
elseif b=='p';
    const=14;
else disp('Invalid Madrak')
    b='x';
end
if b~='x'
    a=input('Input Your Grade: ');
    clc
    if (a>20)||(a<0);
        disp('Enter Grade Between 0 and 20')
    elseif a<const;
        disp('Fail')
    else disp('Pass')
    end
end