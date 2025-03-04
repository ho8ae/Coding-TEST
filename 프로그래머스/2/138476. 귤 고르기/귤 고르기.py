from collections import Counter

def solution(k, tangerine):
    # 초기 설정
    answer = 0
    dic = Counter(tangerine)
    #	Counter({3: 2, 2: 2, 5: 2, 1: 1, 4: 1})
    count = 0
    
    sorted_tangerine = sorted(dic.items(),key= lambda x: -x[1])
    
    if sorted_tangerine[0][1]> k:
            count +=1
            return count
    
    
    for ten_key, ten_value in sorted_tangerine:
        answer += ten_value
        count += 1
        if answer >= k:
            return count
            
    