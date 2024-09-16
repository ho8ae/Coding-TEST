n = int(input())

g=[]
g=(list(map(int,input().split())))

    
g.sort(reverse=True)

topLv = g[0]
total = 0
for i in range(1,n):
    total += topLv + g[i]

print(total)