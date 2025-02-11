### 1890 점프

n = int(input())

arr= [[0]*(n+1)]

for _ in range(n):
    arr.append([0]+list(map(int,input().split())))
dp = [[0]*(n+1) for _ in range(n+1)]
dp[1][1] = 1

for i in range(1,n+1):
    for j in range(1,n+1):
        if dp[i][j] > 0 and arr[i][j] > 0:
            jump = arr[i][j]
            
            if j+jump <= n:
                dp[i][j+jump] += dp[i][j]
            if i+jump <= n:
                dp[i+jump][j] += dp[i][j]

print(dp[n][n])