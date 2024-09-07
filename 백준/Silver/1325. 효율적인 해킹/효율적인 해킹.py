#1325
#한 회사에 N개의 컴퓨터, 회사의 컴퓨는 신뢰한느 컴퓨터 아닌 컴퓨터 관계가 있음
#A가 B를 신뢰하는 경우에는 B를 해킹하면 A도 해킹할 수 있다는 소리다.
#이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램 작성

#입력 - N(컴퓨터 갯수) , M(두번째 줄)

from collections import deque

n,m = map(int,input().split())

g = [[] for _ in range(n+1)] #빈 배열 만들기, 메모리를 최소화함 빈 배열에 값을 넣지 않음으로
ret = []

for _ in range(m):
    a,b=map(int,input().split())
    g[b].append(a)

def bfs(start):
    q=deque()
    q.append(start)
    cnt = 0
    
    visited = [False]*(n+1)
    visited[start] =True
    
    while q:
        cur = q.popleft()
        for next in g[cur]:
            if not visited[next]:
                q.append(next)
                visited[next]=True
                cnt+=1
    return cnt

    
res = []
for start in range(1,len(g)):
    res.append(bfs(start))

for i in range(len(res)):
    if max(res)==res[i]:
        print(i+1)
    
