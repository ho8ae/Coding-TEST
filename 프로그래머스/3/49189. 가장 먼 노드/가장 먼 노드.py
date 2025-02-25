from collections import deque
def solution(n, edge):
    
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    
    # 각 노드의 최단거리 리스트
    distance = [-1] * (n+1) # 방문 리스트
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    q = deque([1]) # 출발 노드
    distance[1] = 0 #+1 한거임
        
    # bfs
    while q:
        cnode = q.popleft()
        
        for nnode in graph[cnode]:
            if distance[nnode] == -1:
                q.append(nnode)
                distance[nnode] = distance[cnode] + 1
    
    for d in distance:
        if d==max(distance):
            answer += 1
    return answer