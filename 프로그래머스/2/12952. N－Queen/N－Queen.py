def dfs(depth):
    global answer,N,v1,v2,v3
    if depth == N:
        answer +=1
        return

    for j in range(N):
        if v1[j]==v2[depth+j]==v3[depth-j]==0:
            v1[j]=v2[depth+j]=v3[depth-j]=1
            dfs(depth+1)
            v1[j]=v2[depth+j]=v3[depth-j]=0
    
def solution(n):
    global answer,N,v1,v2,v3
    answer = 0
    N=n
    v1 = [0]*n
    v2 = [0]*(n*2)
    v3 = [0]*(n*2)
    
    dfs(0)
    
    return answer