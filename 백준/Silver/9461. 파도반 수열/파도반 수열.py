#9461 - 파도반 수열 

T = int(input())

def P(n):
    dp = [1]*n
    
    for i in range(3,n):
        dp[i] = dp[i-2]+dp[i-3]
    
    return dp[n-1]


for _ in range(T):
    n = int(input())
    print(P(n))