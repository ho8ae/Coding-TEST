from itertools import combinations_with_replacement


N,M = map(int,input().split())
lst = list(map(int,input().split()))
set_lst = set(lst)
answer = []

for node in combinations_with_replacement(set_lst,M):
    answer.append(node)

sa = []
for ans in answer:
    sa.append(list(ans))
re = []
for s in sa:
    s.sort()
    re.append(s)

re.sort()

for r in re:
    print(*r)