def solution(n):
    # 삼각형 배열 초기화 (각 행마다 열의 개수가 다름)
    v = [[0] * (i+1) for i in range(n)]
    
    # 방향: 아래, 오른쪽, 대각선 위
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    
    num = 1  # 채워넣을 숫자
    x, y = 0, 0  # 시작 좌표
    d = 0  # 시작 방향 (아래)
    
    # 채워야 할 총 칸 수
    total = n * (n + 1) // 2
    
    # 모든 칸이 채워질 때까지 반복
    while num <= total:
        v[x][y] = num
        num += 1
        
        nx = x + dx[d]
        ny = y + dy[d]
        
        # 다음 위치가 범위를 벗어나거나 이미 채워진 경우 방향 전환
        if nx < 0 or nx >= n or ny < 0 or ny > nx or v[nx][ny] != 0:
            d = (d + 1) % 3
            nx = x + dx[d]
            ny = y + dy[d]
        
        x, y = nx, ny
    
    # 결과를 1차원 배열로 변환하여 반환
    
    answer = []
    for i in range(n):
        for j in range(len(v[i])):
            answer.append(v[i][j])
    
    return answer