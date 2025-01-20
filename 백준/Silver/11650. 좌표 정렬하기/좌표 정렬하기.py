### 11650

N = int(input())

arr = []

for _ in range(N):
    arr.append(list(map(int,input().split())))

sorted_arr = sorted(arr)

for arr in sorted_arr:
    print(arr[0],arr[1])
    
