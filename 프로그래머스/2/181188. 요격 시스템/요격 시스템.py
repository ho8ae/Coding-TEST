def solution(targets):
    targets = sorted(targets,key=lambda x: x[0])
    
    answer = 1
    aim_start,aim_end = targets.pop(0)
    
    for target in targets:
        target_start,target_end = target
        if aim_end > target_start:
            aim_start = max(aim_start,target_start)
            aim_end = min(aim_end,target_end)
        else:
            aim_start,aim_end = target_start,target_end
            answer +=1
    
    
    return answer