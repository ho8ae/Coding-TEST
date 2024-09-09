
from collections import deque



def bfs(i,j,h):
    q =  deque()
    
    q.append((i,j))
    v[i][j]=1
    
    while q:
        x,y = q.popleft()
        for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
            nx,ny= x+dx , y+dy
            if 0<=nx<N and 0<=ny<N and v[nx][ny] ==0 and arr[nx][ny]>h:
                q.append((nx,ny))
                v[nx][ny]=1
    



def solve(h): #높이에 대해 잠기지 않는 영역 개수 리턴
    cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] ==0 and arr[i][j] > h:
                bfs(i,j,h)
                cnt+=1
    return cnt




N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]  # Corrected this line

ans = 0
for h in range(100): #높이 0~99 까지 물 높이 지정
    v = [[0]*N for _ in range(N)]
    ans = max(ans,solve(h))
print(ans)
               