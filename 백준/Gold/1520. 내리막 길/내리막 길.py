import sys
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())
# [[0, 0, 0, 0, 0, 0, 0],
#  [0, 50, 45, 37, 32, 30, 0],
#  [0, 35, 50, 40, 20, 25, 0],
#  [0, 30, 30, 25, 17, 28, 0],
#  [0, 27, 24, 22, 15, 10, 0],
#  [0, 0, 0, 0, 0, 0, 0]]

# 범위체크를 생략하기 위해서 0으로 둘러쌈
arr = [[0]*(m+2)]+[[0]+list(map(int,sys.stdin.readline().split()))+[0] for _ in range(n)]+[[0]*(m+2)]

dp = [[-1]*(m+2) for _ in range(n+2)]
dp[1][1] = 1

def dfs(ci,cj):
    if dp[ci][cj] == -1: # 계산 되어 있지 않다면(첫방문) 계산 후 저장
        # 네방향(더 높은 곳으로부터 낮은 곳 방문 시 경로 수 누적)
        dp[ci][cj] =0 
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            pi,pj = ci+di, cj+dj # 이전좌표 네 방향 계산
            if arr[pi][pj] > arr[ci][cj]: # 높은 곳 -> 낮은 곳
                dp[ci][cj] += dfs(pi,pj)  # 조건에 맞는 네 방향 경로수 누적
    return dp[ci][cj]
            
            
        


print(dfs(n,m))