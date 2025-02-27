from collections import deque

def bfs(start_idx,N,lst):
    
    v= [-1]*(N+1) # 방문 배열 초기화
    v[start_idx] = 0
    
    q = deque([start_idx])
    
    while q:
        c = q.popleft()
        
        for node in lst[c]:
            if v[node] ==-1:
                v[node] = v[c]+1
                q.append(node)

                
    return v

def solution(n, roads, sources, destination):
    answer = []
    lst = [[] for _ in range(n+1)]
    
    # lst 초기 설정
    for node in roads: # 1,2
        lst[node[0]].append(node[1])
        lst[node[1]].append(node[0])
    
    # 목적지에서 시작하는 BFSf
    distances = bfs(destination,n,lst)
    
    for source in sources:
        answer.append(distances[source])
  
    
    return answer