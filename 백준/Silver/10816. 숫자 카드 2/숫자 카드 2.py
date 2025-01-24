from collections import Counter

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

count = Counter(N_list)
print(*(count[m] for m in M_list))