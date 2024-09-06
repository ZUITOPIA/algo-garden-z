m, n = map(int, input().split())
arr = list(map(int, input().split()))

start = 1  # 과자의 최소 길이
end = max(arr)
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = 0

    for value in arr:
        if value < mid:
            continue
        else:
            count += value // mid

    if count >= m:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)