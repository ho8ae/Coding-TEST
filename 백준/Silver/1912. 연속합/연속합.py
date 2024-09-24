n = int(input())
g= list(map(int,input().split()))
current_max = g[0]
global_max = g[0]
for i in range(1,n):
    current_max = max(g[i],current_max+g[i])
    global_max = max(global_max,current_max)
print(global_max)