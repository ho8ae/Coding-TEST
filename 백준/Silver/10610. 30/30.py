n = list(input())
n

if '0' in n:
    sumAll = 0
    for num in n:
        sumAll += int(num)
    if sumAll % 3 == 0:
        n.sort(reverse=True)
        
        for num in n:
            print(num,end='')
    else:
        print(-1)
else:
    print(-1)