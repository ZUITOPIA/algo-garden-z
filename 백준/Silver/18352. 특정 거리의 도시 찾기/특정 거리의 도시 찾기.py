from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
distance = [0]*(n+1)


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # 단방향


def bfs(start):
    result = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0

    while q:
        temp = q.popleft()
        for i in graph[temp]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[temp] + 1
                if distance[i] == k:
                    result.append(i)

    if len(result) == 0:
        print(-1)
    else:
        result.sort()
        for i in result:
            print(i)



bfs(x)