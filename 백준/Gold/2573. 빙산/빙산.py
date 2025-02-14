# 2573




def bfs(ci,cj,v):
    # bfs 덩어리 개수 세기
    
    q = []
    q.append((ci,cj))
    v[ci][cj] = -1
    
    while q:
        ci,cj = q.pop(0)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj] != -1 and v[ni][nj] != 0:
                v[ni][nj] = -1
                q.append((ni,nj))
    return 1

def solve():
    year_count = 0 
    
    # [1] 덩어리 세기
    while 1:
        # v = arr 이렇게 복사하면 주소가 복사되어서 안됨
        v = [row[:] for row in arr]  # 방문배열 복사
        dung_count = 0
        
        
        for i in range(N):
            for j in range(M):
                # if v[i][j] != 0 and v[i][j] != -1:
                 if v[i][j] > 0: # 간단하게 이렇겍 ㅏ능
                    dung_count += bfs(i,j,v)

        # if dung_count == 2: # 빙산이 2개 이상이어야함
        if dung_count >= 2: # 두 덩어리 이상이 나오는 경우
            return year_count
        
        if dung_count == 0: # 빙산이 다 녹았을 때
            return 0 
        
        flag = 1
        
    # [2] 빙산 녹이기
        melt = [[0]*M for _ in range(N)]
    
        while flag == 1:
            for i in range(N):
                for j in range(M):
                    if arr[i][j] > 0:
                        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                            ni,nj = i+di,j+dj
                            if arr[ni][nj] == 0:
                                melt[i][j] += 1
            
            for i in range(N):
                for j in range(M):
                    arr[i][j] = max(0,arr[i][j] - melt[i][j])
            
            year_count += 1
            flag = 0
        
    

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = solve()
print(ans)