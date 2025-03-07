def solution(storage, requests):
    global n, m, v
    n, m = len(storage), len(storage[0])
    
    # 2차원 리스트로 변환 및 외부 테두리 추가
    grid = []
    grid.append(["0"] * (m + 2))  # 상단 테두리
    for row in storage:
        grid.append(["0"] + list(row) + ["0"])  # 좌우 테두리 추가
    grid.append(["0"] * (m + 2))  # 하단 테두리
    
    # v 배열 초기화: -1은 컨테이너, 0은 외부와 연결된 공간, 1은 막힌 빈 공간
    v = [[-1 for _ in range(m + 2)] for _ in range(n + 2)]
    for i in range(n + 2):
        for j in range(m + 2):
            if grid[i][j] == "0":
                v[i][j] = 0  # 외부와 연결된 공간
    
    
    
    def update_external(x, y):
        # 컨테이너가 제거된 후 외부와 연결된 공간 업데이트
        if v[x][y] != 0:
            v[x][y] = 0  # 외부와 연결
            
            # 인접한 공간 확인
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n + 2 and 0 <= ny < m + 2:
                    if v[nx][ny] == 1:  # 빈 공간이라면
                        update_external(nx, ny)  # 재귀적으로 연결
    
    for request in requests:
        # 크레인인 경우 (길이가 2)
        if len(request) == 2:
            target = request[0]
            
            # 모든 해당 종류 컨테이너 제거
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if grid[i][j] == target:
                        grid[i][j] = "1"  # 빈 공간으로 변경
                        v[i][j] = 1  # 빈 공간 표시
                        
                        # 외부와 연결됐는지 확인
                        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                            nx, ny = i + dx, j + dy
                            if v[nx][ny] == 0:  # 인접한 곳이 외부와 연결되어 있다면
                                update_external(i, j)  # 현재 위치도 외부와 연결
                                break
        
        # 지게차인 경우 (길이가 1)
        else:
            target = request[0]
            to_remove = []
            
            # 접근 가능한 컨테이너 찾기
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if grid[i][j] == target:
                        # 외부와 연결된 공간에 인접해 있는지 확인
                        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                            nx, ny = i + dx, j + dy
                            if v[nx][ny] == 0:  # 외부와 연결된 공간에 인접
                                to_remove.append((i, j))
                                break
            
            # 제거할 컨테이너들 제거
            for i, j in to_remove:
                grid[i][j] = "1"  # 빈 공간으로 변경
                v[i][j] = 1  # 빈 공간 표시
                
                # 외부와 연결됐는지 확인
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nx, ny = i + dx, j + dy
                    if v[nx][ny] == 0:  # 인접한 곳이 외부와 연결되어 있다면
                        update_external(i, j)  # 현재 위치도 외부와 연결
                        break
    
    # 남은 컨테이너 수 계산
    answer = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if v[i][j] == -1:  # 아직 컨테이너가 남아있는 경우
                answer += 1
    
    return answer