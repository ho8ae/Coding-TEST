from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]


    
def bfs(g,a,b):
    n = len(g)
    queue=deque()
    queue.append((a,b))
    g[a][b]=0
    count = 1 #1이 몇 개 있는지 카운트
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y + dy[i]
            if nx<0 or nx>= n or ny<0 or ny>=n:
                continue
            if g[nx][ny] == 1:
                g[nx][ny]=0
                queue.append((nx,ny))
                count += 1
    return count
    
n = int(input())
g =[]
for _ in range(n):
    g.append(list(map(int,input())))
cnt= []
for i in range(n):
    for j in range(n):
        if g[i][j]==1:
            cnt.append(bfs(g,i,j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])
