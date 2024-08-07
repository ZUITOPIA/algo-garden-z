from collections import deque

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]

color_blind_array = [['R' if char == 'G' else char for char in line] for line in arr]  # 입력받은 배열을 이용하여 적록 색약용 배열을 따로 생성

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(array, visited, start): # 탐색할 배열, 그 배열의 방문 여부, BFS 탐색을 시작할 좌표의 행 열을 나타내는 튜플 자체
    queue = deque([start])
    visited[start[0]][start[1]] = True   # 시작점을 True로 바꾸고 시작
    color = array[start[0]][start[1]]  # 시작점 색상 미리 꺼내두기

    while queue:
        x, y = queue.popleft()  # 현재 좌표 꺼내기
        for dx, dy in directions:
            nx, ny = x + dx, y + dy  # 인접 좌표 계산하기
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and array[nx][ny] == color:
                visited[nx][ny] = True  # 방문했음을 표시
                queue.append((nx, ny))  # 새로운 좌표 추가


def count_regions(array):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(array, visited, (i, j))
                count += 1
    return count


normal_count = count_regions(arr)
color_blind_count = count_regions(color_blind_array)

print(normal_count, color_blind_count)
