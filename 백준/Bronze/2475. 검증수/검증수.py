arr = list(map(int, input().split()))
sum = 0

for i in range(len(arr)):
    sum += arr[i]**2

n = sum % 10
print(n)