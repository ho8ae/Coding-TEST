import math

def solution(progresses, speeds):
    answer = []
    n=len(progresses)
    #각 작업의 배포 가능일 계산
    days_left = [math.ceil((100-progresses[i])/speeds[i]) for i in range(n)]
    
    count = 0 #배포될 작업의 수 
    max_day = days_left[0] #가장 늦게 배포될 작업의 가능일
    
    for i in range(n):
        if days_left[i]<=max_day:
            count+=1
        else:
            answer.append(count)
            count=1
            max_day=days_left[i]
    answer.append(count)#마지막으로 카운트 된 작업들을 함께 배포
    return answer