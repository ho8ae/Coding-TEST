# 9663 N- Queen

def dfs(n):
    global ans
    if n==N:
        ans+=1
        return
    
    for j in range(N):
        if v1[j]==v2[n+j]==v3[n-j]==0:
            v1[j]=v2[n+j]=v3[n-j]=1
            dfs(n+1)
            v1[j]=v2[n+j]=v3[n-j]=0

N = int(input())

ans = 0
v1 = [0]*N
v2 = [0]*(N*2)
v3 = [0]*(N*2)

dfs(0)

print(ans)