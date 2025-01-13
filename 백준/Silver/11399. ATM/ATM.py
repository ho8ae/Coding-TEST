# 11399 - ATM

n = int(input())
p = list(map(int,input().split()))

p = sorted(p)
pTime = []
pTime.append(p[0])

for i in range(1,n):
    pTime.append(pTime[i-1]+p[i])
    
print(sum(pTime))