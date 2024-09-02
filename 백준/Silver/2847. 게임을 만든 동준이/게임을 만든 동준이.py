n = int(input())
arr = []

for i in range(n):
    arr.insert(0, int(input()))

count = 0

for i in range(1, n):
    if arr[i] >= arr[i-1]:
        difference = arr[i] - arr[i-1] + 1
        arr[i] -= difference
        count += difference

print(count)
