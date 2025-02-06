import sys

N = int(sys.stdin.readline())

sticks = []
for _ in range(N):
    sticks.append(int(sys.stdin.readline()))
    
    
sticks.sort(reverse=True)

result = -1

for i in range(N-2):
    if sticks[i] < sticks[i+1]+sticks[i+2]:
        result = sticks[i]+sticks[i+1]+sticks[i+2]
        break
        
print(result)