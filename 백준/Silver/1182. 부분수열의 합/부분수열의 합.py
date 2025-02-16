# 1182 부분 수열의 합

def dfs(n,sm,cnt):
    global ans
    if n==N:
        if sm==S and cnt>0:
            ans +=1
        return
    
    # 하부 함수 호출
    dfs(n+1,sm+lst[n],cnt+1) # n인 index를 포함 O
    dfs(n+1,sm,cnt) # 포함 x
    
N, S = map(int,input().split())
lst = list(map(int,input().split()))
ans = 0
dfs(0,0,0)
print(ans)