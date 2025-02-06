T, W = map(int, input().split())
plums = [0]  # 1부터 시작하기 위해 0 추가
for _ in range(T):
    plums.append(int(input()))

# dp[시간][이동횟수]
dp = [[0]*(W+1) for _ in range(T+1)]

# 초기값 설정: 처음에는 1번 나무 아래에 있음
for i in range(T+1):
    if plums[i] == 1:  # 1번 나무에서 떨어질 때
        dp[i][0] = dp[i-1][0] + 1
    else:  # 2번 나무에서 떨어질 때
        dp[i][0] = dp[i-1][0]

# dp 채우기
for i in range(1, T+1):  # 시간
    for j in range(1, W+1):  # 이동횟수
        # 현재 위치 계산 (이동횟수가 짝수면 1번 나무, 홀수면 2번 나무)
        current_tree = 2 if j % 2 == 1 else 1
        
        # 자두가 현재 위치의 나무에서 떨어질 경우
        if plums[i] == current_tree:
            dp[i][j] = max(dp[i-1][j] + 1, dp[i-1][j-1] + 1)
        # 다른 나무에서 떨어질 경우
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])

# 최대값 찾기
result = max(dp[T])
print(result)