from collections import deque
# 다익스트라 알고리즘
def solution(N, road, K):
    answer = 0

    lst=[[]*(N+1) for _ in range(N+1)]
    
    for a,b,c in road:
        lst[a].append([b,c])
        lst[b].append([a,c])
        
    v=[float('inf')] *(N+1)
    
    v[1] = 0
    
    q = deque([(1,0)])
    
    while q:
        node,distance = q.popleft()
        
        if v[node] < distance:
            continue
            
        for next_node , weight in lst[node]:
            new_dist = distance + weight
            
            if new_dist < v[next_node]:
                v[next_node] = new_dist
                q.append((next_node,new_dist))
    
    
    for i in range(1,len(v)):
        if v[i] <=K:
            answer += 1
  

    return answer