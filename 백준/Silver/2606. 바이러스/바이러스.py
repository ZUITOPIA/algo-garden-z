n = int(input())
e = int(input())

graph = [[] for i in range(n + 1)]  # 인덱스 1부터
visited = [0] * (n + 1)  # 인덱스 1부터

for _ in range(e):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]  # 양방향 연결

def dfs(v):
    global count
    visited[v] = 1
    count += 1
    for node in graph[v]:
        if not visited[node]:
            dfs(node)

count = 0
dfs(1)
print(count-1)   # 맨 처음 자기 자신은 제외하기 위함
