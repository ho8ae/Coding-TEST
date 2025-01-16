# 1012 - 유기농 배추 BFS 버전

from collections import deque


T = int(input()) # 몇 번의 테스트 케이스

dx = [0,0,-1,1]
dy = [-1,1,0,0]


def BFS(graph,x,y): #bfs 함수 구현
    q = deque()
    q.append([x,y])
    graph[x][y]=0 # 방문 처리 1 -> 0 으로 만들기
    
    while q: # q가 비었다. 탐색 종료 모두 탐색
        x,y=q.popleft()
        for i in range(4): # 상하좌우 탐색
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<M and 0<=ny<N and graph[nx][ny]==1: #배추밭 범위 지나지 않고 1인 경우
                q.append([nx,ny])
                graph[nx][ny]=0


for _ in range(T):
    M,N,K = map(int,input().split())
    graph = [[0]*(N) for _ in range(M)] # 빈 배추밭 만들기
    
    for _ in range(K):
        a,b = map(int,input().split())
        graph[a][b] = 1
    
    cnt = 0
    
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                BFS(graph,i,j)
                cnt +=1 
    
    print(cnt)