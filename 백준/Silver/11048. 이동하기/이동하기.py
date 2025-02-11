n,m = map(int,input().split())
arr = [[0]*(m+1)]
for i in range(n):
    arr.append([0]+list(map(int,input().split())))

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j]= arr[i][j]+max(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])
    
print(dp[n][m])