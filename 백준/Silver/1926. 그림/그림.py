from collections import deque

n, m = map(int, input().split())

g = []

for _ in range(n):
    g.append(list(map(int, input().split())))

def BFS(g, a, b):
    queue = deque()
    queue.append((a, b))
    g[a][b] = 0
    count = 1
    while queue:
        x, y = queue.popleft()
        for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx = x + i
            ny = y + j
            if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 수정된 부분
                continue
            if g[nx][ny] == 1:  # 수정된 부분
                queue.append((nx, ny))
                g[nx][ny] = 0
                count += 1
    return count

cnt = []
total = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == 1:
            cnt.append(BFS(g, i, j))
            total += 1

print(total)
if cnt:
    print(max(cnt))
else:
    print(0)
