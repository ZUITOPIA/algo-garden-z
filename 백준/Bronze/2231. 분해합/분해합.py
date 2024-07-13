n = int(input())
value = 0

for i in range(1, n+1):
    arr = list(map(int, str(i)))  # i가 215라면 arr에는 [2, 1, 5] 형태로 저장됨

    value = i + sum(arr)

    if value == n:
        print(i)
        break
    if i == n:
        print(0)