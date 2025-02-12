# 1987 - 알파벳 BFS 버전 (중복 시퀀스) 이렇게 하면 시간초과가 생김
from collections import deque


def bfs():
    # q 등 필요데이터 생성
    q = deque()
    # v = [[[] for _ in range(m)] for _ in range(n)] # 리스트는 O(n)
    v = [[set() for _ in range(m)] for _ in range(n)] # set는 O(1)
    ans = 1
    
    # q에 초기데이터(들) 삽입
    q.append((0,0,arr[0][0]))
    v[0][0].add(arr[0][0])
    
    while q:
        ci,cj,cv=q.popleft()
        ans = max(ans,len(cv))
        
        # 네 방향, 범위 내 , 중복값이 아닌경우, 중복 시퀀스
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj] not in cv:
                if cv+arr[ni][nj] not in v[ni][nj]:
                    q.append((ni,nj,cv+arr[ni][nj]))
                    v[ni][nj].add((cv+arr[ni][nj]))

    return ans
    
n,m = map(int,input().split())

arr = list(input() for _ in range(n))
ans = bfs()
print(ans)