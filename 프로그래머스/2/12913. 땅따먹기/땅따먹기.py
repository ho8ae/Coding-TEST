def solution(land):
    n,m=len(land),4
    
    dp=[[0]*m for _ in range(n)]
    
    for j in range(4):
        dp[0][j] = land[0][j]
    
    for i in range(1,n):
            dp[i][0] = land[i][0] + max(dp[i-1][1],dp[i-1][2],dp[i-1][3])
            
            dp[i][1] = land[i][1] + max(dp[i-1][0],dp[i-1][2],dp[i-1][3])
            
            dp[i][2] = land[i][2] + max(dp[i-1][1],dp[i-1][0],dp[i-1][3])
            
            dp[i][3] = land[i][3] + max(dp[i-1][1],dp[i-1][2],dp[i-1][0])
    
    return max(dp[-1])