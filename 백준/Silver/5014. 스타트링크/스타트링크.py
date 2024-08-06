# 문제 : 눌러야 하는 버튼의 수의 최소값 -> BFS 써야겠다
# 이 문제는 1차원 상에서 앞 뒤로만 움직이는 문제임!

from collections import deque

n, start, goal, up, down = map(int, input().split())

arr = [0]*(n+1)
visited = [False]*(n+1)

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        if v == goal:
            return arr[goal]
        for next in v+up, v-down:
            if 0 < next <= n and not visited[next]:
                visited[next] = True
                arr[next] = arr[v] + 1
                q.append(next)  # 값 추가
    if arr[goal] == 0:
        return "use the stairs"

print(bfs(start))