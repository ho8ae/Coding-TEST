# 11057 - 오르막 수 

n = int(input())
dp = [[0]*10 for _ in range(n+1)]


for i in range(10):
    dp[1][i] = 1

for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
            
print(sum(dp[n])%10007)