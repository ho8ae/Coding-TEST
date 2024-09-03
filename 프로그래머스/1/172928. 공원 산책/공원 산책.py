def solution(park, routes):
    r = {"S": [1, 0], "N": [-1, 0], "E": [0, 1], "W": [0, -1]}
    route = dict()

    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                x, y = i, j
                #순회 화면서 시작지점 잡기
    for i in routes:
        dx, dy = r[i.split()[0]]
        n = int(i.split()[1])
        ix, iy = x, y
        for _ in range(n): #첫 순회 시 E 2 이므로 n은 2번
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= len(park) or ny < 0 or ny >= len(park[0]):
                x, y = ix, iy
                break
                # 장애물 확인 원위치
            if park[nx][ny] == "X":
                x, y = ix, iy
                break
                # 도착지점 확인 원위치
            x, y = nx, ny
    return [x, y]