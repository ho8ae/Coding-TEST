#2571 수 정렬하기2
# N개의 수가 주어졌을 대, 이를 오름차순으로 정렬하는 프로그램 작성

import sys

n = int(sys.stdin.readline())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline().strip()))
numbers.sort()
print('\n'.join(map(str, numbers)))
                   