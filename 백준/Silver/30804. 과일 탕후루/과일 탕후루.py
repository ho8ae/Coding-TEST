# 30804 - 탕후루

N = int(input())
arr = list(map(int, input().split()))

left = 0
count_dict = {}
max_len = 0

for right in range(N):
    current_fruit = arr[right]
    
    if current_fruit in count_dict:
        count_dict[current_fruit] +=1
    else:
        
        count_dict[current_fruit] = 1
                   
    while len(count_dict) > 2:
        fruit_to_remove = arr[left]
        count_dict[fruit_to_remove] -= 1
        
        if count_dict[fruit_to_remove] == 0:
            del count_dict[fruit_to_remove]
        
        left += 1
    
    max_len = max(max_len,right-left+1)

print(max_len)

                       
                   
