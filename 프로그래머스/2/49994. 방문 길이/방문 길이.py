def is_valid_move(nx, ny):  # 좌표평면을 벗어나는지 체크
    return 0 <= nx < 11 and 0 <= ny < 11

def update_location(x, y, dir):  # 명령어를 통해 다음 좌표설정
    if dir == 'U':
        nx, ny = x, y + 1
    elif dir == 'D':
        nx, ny = x, y - 1
    elif dir == 'R':
        nx, ny = x + 1, y
    elif dir == 'L':
        nx, ny = x - 1, y
    return nx, ny

def solution(dirs):
    x, y = 5, 5
    ans = set()  # 겹치는 좌표는 1개로 처리하기 위해

    for dir in dirs:  # 주어진 명령어로 움직이면서 좌표저장
        nx, ny = update_location(x, y, dir)
        if not is_valid_move(nx, ny):
            continue
        # A ~ B and B ~ A add too
        ans.add((x, y, nx, ny))
        ans.add((nx, ny, x, y))
        x, y = nx, ny  # location update
    return len(ans) // 2

# 예제 호출
print(solution("ULURRDLLU"))  # 예상 결과: 7
