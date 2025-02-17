# 1309 - 동물원

N = int(input())

dp = [0]*(1000001)

dp[0] = 1
dp[1] = 3
dp[2] = 7

for j in range(3,N+1):
    dp[j] = ((dp[j-1]+dp[j-2]) + dp[j-1])%9901

print(dp[N]%9901)