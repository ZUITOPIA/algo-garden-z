from collections import deque   # bfs를 사용하기 위한 queue

n,m = map(int, input().split())  # 행, 열 입력받기
maze = []
for _ in range(n):
    maze.append(list(map(int, input().strip())))

visited = [[False] * m for _ in range(n)]

queue = deque([(0,0,1)])   # 초기 요소를 포함하는 리스트로 deque 초기화 하는 방법 !!!!

dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1]

visited[0][0] = True   # 시작 위치는 이미 방문했으니 True로 초기화 해두기

while queue:
    x, y, distance = queue.popleft()
    if x == n-1 and y == m-1:
        print(distance)
        break

    for i in range(4):  # 상하좌우로 이동해야되기 때문에 4
        nx = x + dx[i]
        ny = y + dy[i]

        # 다음 위치가 미로 범위를 벗어나거나, 이동할 수 없는 곳 (0)이면 지나가기
        if nx < 0 or nx >=n or ny < 0 or ny >= m:
            continue
        if visited[nx][ny] or maze[nx][ny] == 0:
            continue

        # 다음 위치 방문 처리 + 큐에 넣기
        visited[nx][ny] = True
        queue.append((nx,ny,distance+1))


# BFS의 특성상 처음 발견된 위치의 거리가 최단 거리