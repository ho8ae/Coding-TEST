def solution(record):

    answer = []
    dic = {}
    
    # 맵핑하여 ID에 맞게 닉네임정리
    for line in record:
        cmd = line.split(" ")
        if cmd[0] != "Leave":
            dic[cmd[1]] = cmd[2]
    
    # 조건에 맞게 dic 출력
    for line in record:
        cmd =line.split(" ")
        if cmd[0] == "Enter":
            answer.append(dic[cmd[1]]+"님이 들어왔습니다.")
        if cmd[0] == "Change":
            pass
        if cmd[0] == "Leave":
            answer.append(dic[cmd[1]]+"님이 나갔습니다.")
    
    return answer