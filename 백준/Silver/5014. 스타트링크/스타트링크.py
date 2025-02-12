# 5014 
from collections import deque

def bfs(s,e):
    q = deque()
    v = [0]*(F+1)
    
    
    q.append(s)
    v[s] = 1
    
    while q:
        c= q.popleft()
        if c==e:
            return v[c]-1
        
        
        for n in (c+U,c-D):
            if 1<=n<F+1 and v[n]==0:
                q.append(n)
                v[n]=v[c]+1
    return -1


F,S,G,U,D = map(int,input().split())
answer = bfs(S,G)
if answer == -1:
    print('use the stairs')
else:
    print(answer)