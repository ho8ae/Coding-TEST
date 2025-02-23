from itertools import combinations

def solution(n, q, ans):
    # 1. 가능한 모든 조합 생성 (1~n에서 5개 선택)
    candidates = list(combinations(range(1,n+1),5))
    result = 0
    
    # 2. 각 후보 조합에 대해
    
    for candidate in candidates:
        is_vaild = True
        
        # 3. 모든 시도(q)와 비교
        for attempt,correct_count in zip(q,ans): # 
            common_count = len(set(attempt) & set(candidate)) #
            
            if common_count != correct_count:
                is_vaild = False
                break
            
        if is_vaild:
            result += 1
    
    return result