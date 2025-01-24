N = int(input())
N_list = list(map(int,input().split()))
M = int(input())
M_list = list(map(int,input().split()))

# 미리 N_list를 순회하며 카운트
count_dict = {}
for num in N_list:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# M_list의 각 숫자에 대해 카운트 출력
print(*(count_dict.get(m, 0) for m in M_list))