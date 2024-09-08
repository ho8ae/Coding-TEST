n = int(input())
g = []
num = []  # 리스트 선언 시 [] 필요

for _ in range(n):
    g.append(list(map(int, input().strip())))  # 입력 처리

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:  # 범위 체크
        return False
    
    if g[x][y] == 1:  # 조건 만족 시 DFS 진행
        global count
        count += 1
        g[x][y] = 0  # 방문한 곳은 0으로 설정
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False

count = 0
total = 0
for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            num.append(count)  # count 저장
            total += 1
            count = 0  # count 초기화
 
num.sort()
print(total)  # result 대신 total 출력
for i in range(len(num)):
    print(num[i])
