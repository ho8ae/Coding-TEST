# 10815 숫자 카드 - 이분 탐색으로 찾아야함 # 탐색을 하려면 정렬은 필수 !

N = int(input())
Nlst = list(map(int,input().split()))
Nlst.sort()
M = int(input())
Mlst = list(map(int,input().split()))

def search(arr,target):
    left= 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left+right) // 2
        
        if arr[mid] == target:
            return 1
        elif arr[mid]<target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

v = [0]*M

for j in range(M):
    v[j] = search(Nlst,Mlst[j])

print(*v)