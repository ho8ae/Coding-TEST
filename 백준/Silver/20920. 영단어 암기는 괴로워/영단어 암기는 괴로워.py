import sys

N, M = map(int,sys.stdin.readline().split())
lst = {}

# 입력 부분은 동일하게 유지
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if word not in lst:
        lst[word] = 1
    else:
        lst[word] += 1

# 정렬 부분을 한 번에 처리하도록 수정
# -x[1]: 빈도수 내림차순
# -len(x[0]): 단어 길이 내림차순
# x[0]: 알파벳 순
lst = sorted(lst.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

# 출력 부분도 단순화
for word, _ in lst:
    if len(word) >= M:
        print(word)