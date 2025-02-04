N, M = map(int, input().split())
graph = list(map(int,input().split()))
graph.sort()

rs = []

def backtracking(depth):
    if depth == M:
        print(' '.join(map(str,rs)))
        return
    
    for i in range(N):
        if graph[i] in rs:
            continue
        rs.append(graph[i])
        backtracking(depth + 1)
        rs.pop()

backtracking(0)