n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 1 라이언, 2 어피치

start = 0
end = 0
count = 0
result = float("inf")

while end < n:
    if arr[end] == 1:
        count += 1
    end += 1

    while count >= k:
        result = min(result, end - start)

        if arr[start] == 1:
            count -= 1
        start += 1

if result == float("inf"):
    print(-1)
else:
    print(result)