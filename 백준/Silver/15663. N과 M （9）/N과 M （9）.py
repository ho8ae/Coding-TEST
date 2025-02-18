#  15663 N과M (9)

def dfs(n,lst):
    global ans
    if n==M:
        ans.add(tuple(lst))
        return
    
    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1,lst+[arr[j]])
            v[j] = 0 

N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
ans = set()
v = [0]*N
dfs(0,[])

for lst in sorted(ans):
    print(*lst)