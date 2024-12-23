# 11651

N = int(input())
g=[]
for i in range(N):
    x,y =list(map(int,input().split()))
    g.append([y,x])
g_sort = sorted(g)

for x, y in g_sort:
    print(y,x )