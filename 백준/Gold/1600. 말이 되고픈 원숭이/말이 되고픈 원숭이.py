from collections import deque

move_count = int(input())  # 말의 이동 횟수
col, row = map(int, input().split())  # 격자판 가로의 개수를 나타내는 col, 세로의 개수를 나타내는 row 입력받기

# 방향 벡터 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 말의 이동 방향 벡터 (L자 이동)
horse_dx = [-2, -1, 1, 2, 2, 1, -1, -2]
horse_dy = [1, 2, 2, 1, -1, -2, -2, -1]

# 맵 입력
# 2차원으로 입력받기때문에 [ ] 로 감싸주어야 SyntaxError를 피할 수 있음
arr = [list(map(int, input().split())) for _ in range(row)]

# 방문 체크 배열 (3차원: 말의 이동 횟수, 세로, 가로)
visited = [[[False] * col for _ in range(row)] for _ in range(move_count + 1)]
# 1차원 [False] * (h)
# 2차원 [[False] * (h) for _ in range(w)]
# 3차원 [[[False] * (h) for _ in range(w)] for _ in range(move_count)]
# ... 차원을 추가하는 규칙


# BFS 초기 시작점 넣어주기 (x, y, 출력해야할 최소 이동 거리, 말의 이동 횟수)
queue = deque([(0, 0, 0, 0)])
# 초기 시작점 넣어준 후 방문했음을 표시하기
visited[0][0][0] = True

while queue:
    # 큐에 값이 존재하는 동안 반복 수행
    x, y, answer, horse_moves = queue.popleft()
    # 먼저 큐에서 값 꺼내고 그 값을 기준으로 아래 코드 실행

    # 도착 지점에 도달하면 결과 출력 후 종료
    if x == col - 1 and y == row - 1:
        # 가로와 세로의 범위 (index가 0부터 시작)
        print(answer)
        break   # while문 밖으로 빠져나가기

    # 상하좌우 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < col and 0 <= ny < row and not visited[horse_moves][ny][nx] and arr[ny][nx] == 0:
            visited[horse_moves][ny][nx] = True
            queue.append((nx, ny, answer + 1, horse_moves))

    # 말 처럼 이동
    if horse_moves < move_count:
        for i in range(8):
            nx = x + horse_dx[i]
            ny = y + horse_dy[i]

            if 0 <= nx < col and 0 <= ny < row and not visited[horse_moves + 1][ny][nx] and arr[ny][nx] == 0:
                visited[horse_moves + 1][ny][nx] = True
                queue.append((nx, ny, answer + 1, horse_moves + 1))

else:
    # 큐를 모두 탐색했는데 도착지점에 도달하지 못한 경우
    print(-1)
