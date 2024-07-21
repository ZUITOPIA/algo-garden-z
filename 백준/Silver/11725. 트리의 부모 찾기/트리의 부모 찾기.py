import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
parent = [0]*(n+1)

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if parent[n] == 0:
                parent[n] = node
                queue.append(n)

bfs(1)

for i in parent[2:]:
    print(i)