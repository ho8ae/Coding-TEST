import sys
input = sys.stdin.readline

n, k = map(int, input().split())
numbers = input().rstrip()
stack = []
for number in numbers:
    while stack and stack[-1] < number and k > 0: # 하나씩 비교하면서 앞 과 뒤 둘 중에 큰 것만 append
        stack.pop() #작으면 pop을 한다.
        k -= 1
    stack.append(number)
if k>0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))