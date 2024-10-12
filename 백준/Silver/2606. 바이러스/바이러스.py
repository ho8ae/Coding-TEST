from collections import deque
n = int(input())
m = int(input())

g= [[] for _ in range(n+1)]
visited = [0]*(n+1)

for i in range(m):
    a,b = map(int,input().split())
    g[a]+=[b]
    g[b]+=[a]
visited[1] = 1 #1번 부터 시작
Q = deque([1])
while Q:
    c = Q.popleft()
    for nx in g[c]:
        if visited[nx]==0:
            Q.append(nx)
            visited[nx]=1
print(sum(visited)-1)