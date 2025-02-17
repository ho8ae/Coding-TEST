N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*3 for _ in range(N)]

# 첫 번째 집의 비용을 초기값으로 설정
dp[0] = costs[0]

# 두 번째 집부터 마지막 집까지
for i in range(1, N):
    # 빨강(0)을 선택할 경우
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
    # 초록(1)을 선택할 경우
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
    # 파랑(2)을 선택할 경우
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

# 마지막 집에서의 최소 비용
result = min(dp[N-1])
print(result)