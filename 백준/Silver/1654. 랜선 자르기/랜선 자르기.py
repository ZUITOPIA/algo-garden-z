k, n = map(int, input().split())
arr = []

for i in range(k):
    arr.append(int(input()))

start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2
    temp = 0
    for i in arr:
        temp += i // mid

    if temp >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)