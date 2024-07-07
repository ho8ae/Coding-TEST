def solution(N, stages):
    
    #스테이지별 도전자 수 구함
    challenger = [0] * (N+2)
    
    for stage in stages:
        challenger[stage]+=1
    #스테이지별 실패한 사용자 수 계산
    fails ={}
    total = len(stages)
    
    #각 스테이지 순회하며, 실패율 계산
    for i in range(1,N+1):
        if challenger[i] ==0: #도전한 사람 없는 경우, 실패율은 0
            fails[i] = 0
        else:
            fails[i] = challenger[i]/total #실패율 구함
            total-=challenger[i] #실패율을 구하기 위해 현재 스트이지 뺌
            
    result = sorted(fails, key=lambda x : fails[x], reverse=True)
    
    return result
  
