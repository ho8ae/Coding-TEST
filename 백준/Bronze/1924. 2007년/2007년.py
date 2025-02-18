# 1924

day = [31,28,31,30,31,30,31,31,30,31,30,31]
x,y = map(int,input().split())

if x==1 and y==1:
    ans = 1
else:
    ans = sum(day[:x-1])+y

    
if ans % 7 == 0:
    print('SUN')
    
if ans % 7 == 1:
    print('MON')
    
if ans % 7 == 2:
    print('TUE')
    
if ans % 7 == 3:
    print('WED')
    
if ans % 7 == 4:
    print('THU')
    
if ans % 7 == 5:
    print('FRI')
    
if ans % 7 == 6:
    print('SAT')
    
