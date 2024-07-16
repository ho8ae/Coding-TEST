def solution(record):
    answer = []
    uid = {}
    
    for line in record:#record의 줄을 하나씩 처리
        cmd = line.split(" ")  # 글이 띄어져 있는 것으로 구분
        if cmd[0] !="Leave": # Enter or Change인 경우
            uid[cmd[1]]=cmd[2]
    for line in record:
        cmd = line.split(" ")
        #각 상태에 맞는 메세지를 answer에 저장
        if cmd[0] =="Enter":
            answer.append("%s님이 들어왔습니다." % uid[cmd[1]])
        elif cmd[0] == "Change":
            pass
        else:
            answer.append("%s님이 나갔습니다." % uid[cmd[1]])
    return answer
    
    return answer