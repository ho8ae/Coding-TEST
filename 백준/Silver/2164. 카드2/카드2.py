# 2164
from collections import deque

N = int(input())
que = deque([i for i in range(1,N+1)])

for _ in range(N-1):
    que.popleft()
    last= que.popleft()
    que.append(last)

for num in que:
    print(num)