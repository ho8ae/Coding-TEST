def solution(n, times):
    answer = 0
    
    left = 1
    right = max(times)*n #n명을 최대로 받을 수 있는 시간
    
    while left<=right:
        
        mid = (left+right)//2
        #심사한 사람 수
        people =  0
        
        for time in times:
            people += mid//time
            
            if people >= n:
                break
        
        if people >= n:
            answer = mid
            right = mid -1
        else:
            left = mid + 1
            
    
    return answer