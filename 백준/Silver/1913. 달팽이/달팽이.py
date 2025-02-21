# 하 우 상 좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def print_arr(arrs):
    for i in range(len(arrs)):
        for j in range(len(arrs[0])):
            print(arrs[i][j], end=" ")
        print()

n = int(input())
m = int(input())

arr = [[0] * n for i in range(n)]

now = n*n

x = 0
y = 0
d = 0
ax = 0
ay = 0

while now > 0:
    arr[x][y] = now

    # 좌표를 찾고자 하는 값이라면
    if now == m:
        ax = x + 1
        ay = y + 1

    now -= 1

    nx = x + dx[d]
    ny = y + dy[d]

    # 다음 위치가 범위를 벗어남 or 이미 채워진 경우
    if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[nx][ny] != 0:
        # 방향을 바꿔줌
        d = (d + 1) % 4

    x = x + dx[d]
    y = y + dy[d]


print_arr(arr)
print(ax, ay)