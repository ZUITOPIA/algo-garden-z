# 문제 : 가장 빠른 시간 몇 초 ? -> BFS 써야겠다
# BFS는 queue 사용함

from collections import deque

n, k = map(int, input().split())  # n: 수빈이의 위치, k: 동생의 위치
MAX = 10**6+1
arr = [0]*MAX

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return arr[v]
        for next in v-1, v+1, 2*v:
            if 0 <= next < MAX and not arr[next]:
                arr[next] = arr[v]+1
                q.append(next)

print(bfs(n))