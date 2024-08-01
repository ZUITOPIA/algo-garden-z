n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

result_arr = []

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, depth):
    depth += 1
    visited[start] = True

    if start == p2:
        result_arr.append(depth)

    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth)

dfs(p1, 0)

if len(result_arr) == 0:
    print(-1)
else:
    print(result_arr[0]-1)
