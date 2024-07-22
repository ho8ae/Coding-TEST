def dfs(computers,visited,node):
    visited[node] = True;
    for idx,connected in enumerate(computers[node]):
        if connected and not visited[idx]: # 연결되어 있으며 방문하지 않는 노드라면
            dfs(computers,visited,idx)


def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(computers,visited,i)
            answer+=1
    return answer