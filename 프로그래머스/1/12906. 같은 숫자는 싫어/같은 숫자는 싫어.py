def solution(arr):
    answer=[]
    current_value=arr[0]
    n=len(arr)
    answer.append(current_value)
    for i in range(1,n):
        if arr[i] != current_value:
            current_value=arr[i]
            answer.append(current_value)
    
    return answer