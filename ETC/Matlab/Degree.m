clc
clear
close all
%%
for i=1:5
    b=input('input Your Degree ( b or m or p ): ','s');
    clc
    if b=='b';
        const=10;
    elseif b=='m';
        const=12;
    elseif b=='p';
        const=14;
    else disp('Invalid Degree')
        b='x';
    end
    if b~='x'
        a=input('input Your Grade: ');
        clc
        if (a>20)||(a<0);
            disp('Enter Grade Between 0 and 20')
        elseif a<const;
            disp('Mardood')
        else disp('Ghabool')
        end
    end
end