from collections import deque
# 방향 전환이 될떄 +1 
def solution(board):
    answer = 0
    n,m = len(board),len(board[0])
    
    # 초기 설정 시작 지점, deque, set을 이용 방향
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                startx,starty = i,j
    # 상, 하, 좌, 우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    q = deque([(startx,starty,0)])  #x,y,카운트
    v = set([(startx,starty)])
    
    
    
    while q:
        x,y,c = q.popleft() 
        
        
        # 종료 조건
        if board[x][y] == 'G':
            return c
        
        for i in range(4):
            nx = x
            ny = y
            while True:
                #빙판길 미끄러지기
                nx = nx + dx[i]
                ny = ny + dy[i]
                
                # 벽을 만나면 방향 전환
                if  0 >nx or nx >= n or 0>ny or ny>=m or board[nx][ny] == 'D':
                    nx = nx-dx[i]
                    ny = ny-dy[i]
                    break
            
            if(nx,ny) not in v:
                v.add((nx,ny))
                q.append((nx,ny,c+1))
                
                
            
            
            
    return -1