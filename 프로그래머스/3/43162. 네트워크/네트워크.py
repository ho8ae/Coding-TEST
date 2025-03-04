def dfs(computers,v,node):
    v[node] = True
    for idx,j in enumerate(computers[node]):
        if j==1 and not v[idx]:
            dfs(computers,v,idx)

def solution(n, computers):
    answer = 0
    v= [False] *n
    
    for i in range(len(v)):
        if not v[i]:
            dfs(computers,v,i)
            answer += 1
    
    return answer