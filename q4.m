clear all;
clc;
close all;
w1 = [2 7; 8 1; 7 5; 6 3; 7 8; 5 9; 4 5;];
w2 = [4 2; -1 -1; 1 3; 3 -2; 5 3.25; 2 4; 7 1;];
x = [2 4; 8 -1; 7 1; 6 3; 7 5; 5 2; 4 7;];
y = [7 2; 1 -1; 5 3; 3 -2; 8 3.25; 9 4; 5 1;];
szw1 = size(w1);
Y =ones(14,3);

for i=1:szw1(1)
    Y(i,2) = w1(i,1);
    Y(i,3) = w1(i,2);
    Y(szw1(1)+i,2) = w2(i,1) * -1;
    Y(szw1(1)+i,3) = w2(i,2) * -1;
end

Y(8:14,1)=-1;
a = [1 1 1];

flag = 0;
n = 1;
b = 0.5;
theta = 0.2;

c = 0;
while 1
    c = c+1;
    for j = 1:14
        n = n/c;
        gx1 = a(1) .* Y(j,1);
        gx2 = a(2) .* Y(j,2);
        gx3 = a(3) .* Y(j,3);
        gx = gx1+gx2+gx3;
        
        d = (n* (b-gx)) * Y(j,:); 
        a = a + d;
        
        if (abs(d) < theta)
            flag = 1;
            break;
        end
    end
    
    if (flag > 0)
        break;
    end
end

figure
%hold on;
xl = -5:15;
yl = -a(1)/a(3)-(a(2)/a(3))*xl;
plot(x,y, '*',xl,yl,'g');


