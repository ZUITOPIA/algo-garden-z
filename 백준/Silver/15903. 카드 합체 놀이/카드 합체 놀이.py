import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))

heapq.heapify(arr)  # 최소 힙 (작은 것 부터 정렬하는 효과)

for _ in range(m):
    if len(arr) > 1:
        a = heapq.heappop(arr)  # 가장 작은 값
        b = heapq.heappop(arr)  # a 다음으로 작은 값
        count = a + b

        heapq.heappush(arr, count)
        heapq.heappush(arr, count)

print(sum(arr))
