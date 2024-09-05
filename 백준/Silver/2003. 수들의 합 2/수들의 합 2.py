n, m = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
start, end = 0, 0
part_sum = 0

while end < n:
    part_sum += arr[end]
    end += 1

    while part_sum >= m:
        if part_sum == m:
            count += 1

        part_sum -= arr[start]
        start += 1

print(count)