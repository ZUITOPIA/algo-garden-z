from collections import deque

m, n, k = map(int, input().split())  # n x m - [y][x]
arr = [[0]*n for _ in range(m)]

result_arr = []

def bfs(x, y):
    q = deque([[x, y]])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    count = 1  # 시작 포함
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                q.append([nx, ny])
                count += 1
    return count

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            arr[i][j] = 1
            result_arr.append(bfs(i, j))

print(len(result_arr))
print(*sorted(result_arr))
