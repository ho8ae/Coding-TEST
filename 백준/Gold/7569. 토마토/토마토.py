from collections import deque

def bfs():
    q = deque()
    # 처음 익은 토마토를 모두 큐에 넣기
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if box[h][i][j] == 1:
                    q.append((h,i,j))
    
    while q:
        h,i,j = q.popleft()
        
        for dh,di,dj in ((-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)):
            nh,ni,nj = h+dh,i+di,j+dj
            if 0<=nh<H and 0<=ni<N and 0<=nj<M and box[nh][ni][nj] == 0:
                box[nh][ni][nj] = box[h][i][j] + 1
                q.append((nh,ni,nj))

M,N,H = map(int,input().split()) # M 열, N 행, H 높이
box = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

bfs()

# 결과 확인      
answer = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if box[h][i][j] == 0:  # 안 익은 토마토가 있다면
                print(-1)
                exit()  # 프로그램 종료
            answer = max(answer, box[h][i][j])
                
print(answer-1)