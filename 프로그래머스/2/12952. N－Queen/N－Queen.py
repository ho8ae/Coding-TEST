def getAns(n, y, width, diagonal1, diagonal2):
    ans = 0
    # 모든 행에 대해서 퀸의 위치가 결정되었을 경우
    if y == n:
        ans += 1
    else:
        # 현재 행에서 퀸이 놓일 수 있는 모든 위치를 시도
        for i in range(n):
            # 해당 위치에 이미 퀸이 있는 경우, 대각선상에 퀸이 있는 경우 스킵
            if width[i] or diagonal1[i + y] or diagonal2[i - y + n]:
                continue
            # 해당 위치에 퀸을 놓음
            width[i] = diagonal1[i + y] = diagonal2[i - y + n] = True
            # 다음 행으로 이동하여 재귀적으로 해결 가능한 경우의 수 찾기
            ans += getAns(n, y + 1, width, diagonal1, diagonal2)
            # 해당 위치에 놓인 퀸을 제거함
            width[i] = diagonal1[i + y] = diagonal2[i - y + n] = False
    return ans

def solution(n):
    # getAns 함수 호출하여 해결 가능한 경우의 수 찾기
    answer = getAns(n, 0, [False] * n, [False] * (n * 2), [False] * (n * 2))
    return answer
