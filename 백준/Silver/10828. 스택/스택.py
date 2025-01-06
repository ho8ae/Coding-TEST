#10828
from collections import deque 
import sys

N = int(sys.stdin.readline())
#이렇게 readline()으로 처리하면 시간초과를 피할 수 있음
Q = deque()

for i in range(N):
    answer = sys.stdin.readline().split()
    
    if answer[0] == 'push':
        Q.append(answer[1])
    if answer[0] == 'top':
        if Q:
            print(Q[-1])
        else:
            print(-1)
    if answer[0] == "pop":
        if Q:
            print(Q.pop())
        else:
            print(-1)
    if answer[0] == 'empty':
        print(1 if not Q else 0)
    if answer[0] == 'size':
        print(len(Q))
    
