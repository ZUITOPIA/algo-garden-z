import sys
from collections import deque

a, b = map(int, input().split())

def bfs(start, count):
    queue = deque([(a, 0)])

    while queue:
        now, count = queue.popleft()
        if now == b:
            print(count+1)
            return
        if now * 2 <= b:
            queue.append((now*2, count+1))
        if now * 10 + 1 <= b:
            queue.append((now*10+1, count+1))
    print(-1)

bfs(a,b)