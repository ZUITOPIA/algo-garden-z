n, m = map(int, input().split())
temp = list(map(int, input().split()))
temp.sort()

arr = []
prev = 0
visited = [False]*n


def dfs(depth):
    prev = 0
    if depth == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(n):
        if temp[i] != prev and visited[i] == False:
            arr.append(temp[i])
            prev = temp[i]
            visited[i] = True
            dfs(depth+1)
            arr.pop()
            visited[i] = False
dfs(0)
