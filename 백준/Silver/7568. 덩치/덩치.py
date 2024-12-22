#### 7568

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
for i in graph:
    rank =1
    for j in graph:
        if i[0] < j[0] and i[1] < j[1]:
            rank +=1
    print(rank, end=' ')
    