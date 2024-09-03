import heapq, sys
input = sys.stdin.readline

q = heapq

n = int(input())
arr = []

for _ in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))

result = []
arr.sort()
q.heappush(result, arr[0][1])


for start, end in arr[1:]:
    if start < result[0]:
        q.heappush(result, end)
    else:
        q.heappop(result)
        q.heappush(result, end)

print(len(result))

