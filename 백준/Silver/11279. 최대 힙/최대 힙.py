import heapq
import sys

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, -x)
    else:
        if len(heap) != 0:
            print(-heapq.heappop(heap))
        else:
            print(0)