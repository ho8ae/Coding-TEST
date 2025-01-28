# dfs 
# 양방향 그래프가 핵심

n = int(input())
start,end = map(int,input().split())
m = int(input())
family = []

for _ in range(m):
    family.append(list(map(int,input().split())))

graph = [[] for _ in range(n+1)]

for x,y in family:
    graph[x].append(y)
    graph[y].append(x)

visited = [False]*(n+1)
result = -1

def dfs(start,end,cnt):
    global result
    
    if start == end:
        result = cnt
        return
    
    for next_node in graph[start]:
        if not visited[next_node]:
            visited[next_node]=True
            dfs(next_node,end,cnt+1)
visited[start]=True
dfs(start,end,0)
print(result)