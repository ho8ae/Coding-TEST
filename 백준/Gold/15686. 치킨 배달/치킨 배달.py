import sys

N,M = map(int,sys.stdin.readline().split())

min_ans = 999999

home = []

chick = []

for i in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    
    for j in range(N):
        if row[j] == 1:
            home.append((i,j))
        elif row[j] == 2:
            chick.append((i,j))

v = [False] * len(chick)


def dfs(idx,cnt):
    global min_ans
    
    if cnt == M:
        ans = 0
        
        for h in home: # 각 집 좌표 꺼내기
            distance = 999999
            for j in range(len(v)):
                if v[j]:
                    check_num = abs(h[0]-chick[j][0])+abs(h[1]-chick[j][1])
                    distance = min(distance,check_num)
            ans += distance
        min_ans = min(ans,min_ans)
        
        return
    
    for i in range(idx,len(chick)):
        if not v[i]:
            v[i] = True
            dfs(i+1,cnt+1)
            v[i] = False


dfs(0,0)
print(min_ans)