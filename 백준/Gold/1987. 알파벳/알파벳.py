# 1987 - 알파벳
import sys

def dfs(ci,cj,cnt):
    global ans
    ans = max(ans,cnt)
    
    # 네 방향으로 검사
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj = ci+di,cj+dj
        
        if 0<=ni<n and 0<=nj<m and v[ord(arr[ni][nj])] == 0:
            v[ord(arr[ni][nj])] = 1
            dfs(ni,nj,cnt+1)
            v[ord(arr[ni][nj])] = 0


n,m = map(int,sys.stdin.readline().split())

arr = list(sys.stdin.readline() for _ in range(n))
v= [0]*128

ans = 1
v[ord(arr[0][0])] = 1
dfs(0,0,1)
print(ans)