#1874 스택 수열

# 스태엑에 push하는 순서는 반드시 오름차순을 지키도록하자
# 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다.

# 간단한 예시부터 시작 입력 수열 [4,3] 인 경우

# 1) + + + + -[1,2,3] 4 출력 완료
# 2) - [1,2] 3출력 완료 

n=int(input())
target_sequence = [] # 목표 수열
for _ in range(n):
    target_sequence.append(int(input()))


count = 1 # 스택에 넣을 수 
stack = [] # 실제 스택
result = [] # +, - 넣는 배열
is_possible = True # 수열 만들기 가능 여부


for target in target_sequence:
    # 1. target 숫자가 나올 때까지 스택에 Push
    while count <= target:
        stack.append(count)
        result.append('+')
        count+=1
    
    # 2. 스택의 top이 target과 같다면 pop
    if stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        # 3. 스택의 top이 target보다 크다면 불가능
        is_possible=False
        break
# 결과 출력
if is_possible:
    for op in result:
        print(op)
else:
    print('NO')