# 15694 N-M 벡트레킹 문제

def dfs(n,lst):
    if n == M:
        ans.append(lst)
        return # 반복문 탈출
    
    for j in range(1,N+1):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1,lst+[j])
            v[j] = 0

N,M = map(int,input().split())
ans = []
v=[0]*(N+1)

dfs(0,[])

for lst in ans:
    print(*lst)