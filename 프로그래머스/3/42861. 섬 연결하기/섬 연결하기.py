def solution(n, costs):
    costs.sort(key=lambda x:x[2])
    v = set([0])
    answer = 0
    
    while len(v) != n:
        for cost in costs:
            if cost[0] in v and cost[1] in v:
                continue
            elif cost[0] in v or cost[1] in v:
                v.update([cost[0],cost[1]])
                answer +=cost[2] # 가중치 더 합
                break
    return answer