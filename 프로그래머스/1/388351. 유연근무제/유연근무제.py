# 1 to 7 월 to 일
# 모든 시각은 시에 100을 곱하고 분을 더한 정수
# 이벤트 시작일 월요일, 출근 희망 시각이 정각으로 된 입력만 주어짐
# schedules = [700,800,1100]
# startday = 5 5면 금요일임.
# 한명씩 검사하고 출근 시간 < 출근 희망 시각 + 10 을 배열 끝까지
# 했을때 없으면 count += 1
# 단, 주말은 출근 시간 상관없음
def convertTime(n): # 분 단위로 변환
    h = n // 100
    m = n % 100
    return h * 60 + m

def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        s = startday
        schedule = convertTime(schedules[i])
        flag = True
        
        for time in timelogs[i]:
            if s == 6 or s == 7: # 주말 제외
                s += 1
                if s == 8:  # 일요일 지나면 월요일로
                    s = 1
                continue
                
            t = convertTime(time)
            if schedule + 10 < t:   # 지각
                flag = False
                break
            
            s += 1
            if s == 8:  # 일요일 지나면 월요일로
                s = 1
        
        if flag:
            answer += 1

    return answer