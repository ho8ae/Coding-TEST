import sys
sys.setrecursionlimit(10**5)

n, m, k = map(int, input().split())
g = [[0]*m for _ in range(n)]
for i in range(k):
    u, v = map(int, input().split())
    g[u-1][v-1] = 1

visit = [[False]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = 0

def DFS(x, y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if g[nx][ny] == 1 and not visit[nx][ny]:
                visit[nx][ny] = True
                cnt += 1
                DFS(nx, ny)

for i in range(n):
    for j in range(m):
        if g[i][j] == 1 and not visit[i][j]:
            cnt = 1 
            visit[i][j] = True 
            DFS(i, j)
            res = max(res, cnt)

print(res)