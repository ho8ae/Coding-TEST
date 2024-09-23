n = int(input())
g = list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if g[i] < g[j]:
            dp[i] = max(dp[j] + 1, dp[i])
print(max(dp))  # 수정된 부분