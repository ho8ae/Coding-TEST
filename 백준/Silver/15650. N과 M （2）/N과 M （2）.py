# 15650

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 
# 고른 수열은 오름차순이어야 한다.


def dfs(n,lst):
    if n>N:
        if len(lst)==M:
            ans.append(lst)
        return
    dfs(n+1,lst+[n])
    dfs(n+1,lst)

N,M=map(int,input().split())
ans = []
dfs(1,[])
for lst in ans:
    print(*lst)