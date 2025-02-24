def solution(grid):
    n, m = len(grid), len(grid[0])
    visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
    directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]  # 아래, 왼쪽, 위, 오른쪽
    answer = []
    
    def move(r, c, d):
        dx, dy = directions[d]
        return (r + dx) % n, (c + dy) % m
    
    def rotate(d, node):
        if node == 'R':
            d = (d + 1) % 4
        elif node == 'L':
            d = (d - 1) % 4
        # 'S'나 다른 문자일 경우 방향 변화 없음
        return d
    
    for r in range(n):
        for c in range(m):
            for d in range(4):
                if not visited[r][c][d]:
                    cx, cy, cd = r, c, d
                    cnt = 0
                    while not visited[cx][cy][cd]:
                        visited[cx][cy][cd] = True
                        cnt += 1
                        cx, cy = move(cx, cy, cd)
                        cd = rotate(cd, grid[cx][cy])
                    answer.append(cnt)
    
    return sorted(answer)