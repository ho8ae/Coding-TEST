def solution(d, budget):
    
    d.sort()
    count =0
    
    for amount in d:
        if budget<amount:
            break #남은 금액이 더 많다면 종료
        budget -= amount #예산에서 신청한 금액을 차감
        count +=1
    return count if budget >= 0 else count -1