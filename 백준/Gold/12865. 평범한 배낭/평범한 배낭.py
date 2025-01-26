#12865 - 평범한 배당 DP

N,K = map(int,input().split())

wv = [(0,0)]
for i in range(1, N+1):
    w, v = map(int, input().split())
    wv.append((w,v))

dp = [[0]*(K+1) for _ in range(N+1)]



for i in range(1, N+1):
    w, v = wv[i] # wv 물건리스트를 하나씩 순회
    for k in range(1, K+1):
        if k >= w: # 현재 무게가, k 보다 작거나 같을 때
            dp[i][k] = max(dp[i-1][k], dp[i-1][k-w] + v)
        else: # 현재 무게가, k 보다 클 때
            dp[i][k] = max(dp[i-1][k], dp[i][k-1])

print(dp[N][K])