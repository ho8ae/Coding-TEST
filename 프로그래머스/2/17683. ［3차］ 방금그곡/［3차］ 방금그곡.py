# 악보 리스트 C, C#을 위한 악보 리스트 만들기
def parse_sheet(sheet):
    result = []
    i = 0
    
    while i <len(sheet):
        if i+1 < len(sheet) and sheet[i+1] == '#':
            result.append(sheet[i:i+2])
            i+=2
        else:
            result.append(sheet[i])
            i+=1
    return result

def solution(m, musicinfos):
    # (None) 기본값 설정
    answer = "(None)"
    max_play_time = 0  # 가장 긴 재생 시간 저장
    
    # 네오가 들은 멜로디 처리
    neo_notes = parse_sheet(m)
    
    for idx, info in enumerate(musicinfos):
        cmd = info.split(",")
        
        # 시간 계산
        start_h, start_m = map(int, cmd[0].split(':'))
        end_h, end_m = map(int, cmd[1].split(':'))
        total_time = (end_h - start_h) * 60 + (end_m - start_m)
        
        # 악보 확장
        sheet_notes = parse_sheet(cmd[3])
        played_sheet = (sheet_notes * (total_time // len(sheet_notes) + 1))[:total_time]
        
        # 네오의 멜로디 찾기
        # 슬라이딩 윈도우 방식으로 찾기
        for i in range(len(played_sheet) - len(neo_notes) + 1):
            if played_sheet[i:i+len(neo_notes)] == neo_notes:
                # 조건에 맞는 곡을 찾았고, 이 곡의 재생 시간이 현재까지 찾은 곡 중 가장 길거나 첫 번째 곡이면
                if total_time > max_play_time:
                    answer = cmd[2]  # 곡 제목 저장
                    max_play_time = total_time  # 최대 재생 시간 업데이트
                break  # 이 곡에서는 멜로디를 찾았으므로 다음 곡으로 넘어감
    
    return answer