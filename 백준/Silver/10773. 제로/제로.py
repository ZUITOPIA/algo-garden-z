n = int(input())
arr = []

for i in range(n):
    num = int(input())
    if num != 0:
        arr.append(num)
    else:
        if len(arr) != 0:
            arr.pop()

if len(arr) == 0:
    print(0)
else:
    print(sum(arr))