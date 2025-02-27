from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    
    # 시작 위치와 목표 위치 찾기
    start_x, start_y = 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start_x, start_y = i, j
    
    # BFS 수행
    queue = deque([(start_x, start_y, 0)])  # (x, y, 이동 횟수)
    visited = set([(start_x, start_y)])  # 방문한 위치 저장
    
    # 상하좌우 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y, count = queue.popleft()
        
        # 목표 위치에 도달했는지 확인
        if board[x][y] == 'G':
            return count
        
        # 네 방향으로 이동 시도
        for i in range(4):
            nx, ny = x, y
            
            # 해당 방향으로 미끄러지기
            while True:
                nx += dx[i]
                ny += dy[i]
                
                # 벽이나 장애물에 부딪히면 멈춤
                if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == 'D':
                    nx -= dx[i]
                    ny -= dy[i]
                    break
            
            # 새로운 위치가 방문하지 않은 곳이라면 큐에 추가
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, count + 1))
    
    # 목표 위치에 도달할 수 없는 경우
    return -1