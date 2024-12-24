# 1920

N = int(input())
A = list(map(int,input().split()))
M = int(input())
arr = list(map(int,input().split()))

A.sort() # 정렬


# arr의 각 원소별로 이분탐색
for num in arr:
    lt, rt = 0, N -1 # 
    isExist = False
    
    # 이분 탐색 시작
    while lt <= rt:
        mid = (lt + rt) // 2 # 중간 값
        if num == A[mid]:
            isExist = True
            print(1)
            break
        elif num > A[mid]:
            lt = mid +1
        else:
            rt = mid -1 
    if not isExist:
        print(0)
    