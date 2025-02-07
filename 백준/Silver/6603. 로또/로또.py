def dfs(n, s, tlst):
    if n == 6:
        ans.append(tlst)
        return
    
    for j in range(s, N):
        dfs(n+1, j+1, tlst+[lst[j]])
        
while True:
    array = list(map(int, input().split()))
    N = array[0]
    
    if N == 0:
        break
        
    lst = array[1:]
    ans = []
    
    dfs(0, 0, [])
    
    for lst in ans:
        print(*lst)
    print()