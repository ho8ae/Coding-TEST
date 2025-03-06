def solution(n, times):
    answer = 0
    
    left = 0
    right = n*max(times) # 한 창구에서 모든 사람이 가능한 최대 시간
    
    while left<=right:
        mid = (left+right) // 2
        people = 0
        
        for time in times:
            people += (mid//time) #각 창구에서 타임당 가능한 사람 수 
            
            if people >= n:
                break
        
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid +1
        
    
    return answer