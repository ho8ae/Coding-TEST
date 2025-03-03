from collections import deque

def solution(board):
    def bfs(start):
        
        # 북동남서
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        length = len(board)
        visited = [[float('inf')]*length for _ in range(length)]
        visited[0][0] = 0

        q = deque([start]) # x, y, cost, dir
        while q:
            x, y, c, d = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 범위안에 들어오는지 확인 
                if 0 <= nx < length and 0 <= ny < length and board[nx][ny] == 0:
                    # 진행방향에 따른 비용 추가
                    nc = c+100 if i == d else c+600
                    if nc < visited[nx][ny]:
                        visited[nx][ny] = nc
                        q.append([nx, ny, nc, i])
                        
        return visited[-1][-1]
    
    return min([bfs((0, 0, 0, 1)), bfs((0, 0, 0, 2))])