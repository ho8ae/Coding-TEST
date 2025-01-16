# 유기농 배추 dfs 버전

import sys
sys.setrecursionlimit(5000)

def dfs(x,y):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    # 경우의 수 탐색
    
    for i in range(4):
        nx  = x +dx[i]
        ny = y + dy[i]
        
        #범위를 벗어난 경우 pass
        if nx<0 or ny<0 or nx>(n-1) or ny>(m-1): continue
        
        # 배추가 존재하는 경우 1인 경우
        if graph[nx][ny] ==1:
            graph[nx][ny] = 0
            dfs(nx,ny)

t= int(input())
cnt = 0 

for _ in range(t):
    m,n,k=map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b= map(int,input().split())
        graph[b][a] = 1
        
    cnt =0
    
    for i in range(n): # 세로
        for j in range(m): # 가로
            if graph[i][j]==1:
                graph[i][j] ==0
                dfs(i,j)
                cnt +=1
    print(cnt)
