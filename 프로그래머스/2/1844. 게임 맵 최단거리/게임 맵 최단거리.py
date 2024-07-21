from collections import deque

def solution(maps):
    #이동할 수 있는 방향을 나타내는 배열 move 선언
    move = [[-1,0],[0,-1],[0,1],[1,0]]
    
    #맵의 크기를 저장하는 변수 선언
    n = len(maps) #행의 길이
    m= len(maps[0]) #열의 길이
    
    # 거리를 저장하는 배열 dist를 -1로 초기화
    dist= [[-1]*m for _ in range(n)]
    
    #dfs 함수 선언
    def bfs(start):
        #deque선언 , 시작 위치를 deque에 추가
        q=deque([start])
        dist[start[0]][start[1]] =1 #start의 좌표
        
        # deque가 빌 때가지 반복
        while q:
            here = q.popleft() #한 행 전체가 빠져나감
            
            #현재 위치에서 이동할 수 있는 모든 방향
            for direct in move:
                row, column = here[0] + direct[0], here[1]+direct[1]
                
                #이동한 위치가 범위를 벗어난 경우 다음 방향으로 넘어감
                if row<0 or row >= n or column < 0 or column>=m:
                    continue
                    
                #이동한 위치에 벽이 있는 경우 다음 방향으로 넘감
                if maps[row][column] == 0:
                    continue
                
                #이동한 위치가 처음 방문하는 경우, deque에 추가하고 거리 갱신
                if dist[row][column]==-1:
                    q.append([row,column])
                    dist[row][column] = dist[here[0]][here[1]] +1
                    
            #거리를 저장하는 배열 dist 반환
        return dist
    bfs([0,0])
    
    return dist[n-1][m-1]