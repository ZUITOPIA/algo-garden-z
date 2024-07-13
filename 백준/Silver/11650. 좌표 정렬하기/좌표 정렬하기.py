n = int(input())
arr = []

for i in range(n):
    [x, y] = map(int, input().split())
    arr.append([x,y])

arr.sort()  # sorted로는 불가능 !!!!

for i in arr:
    print(i[0], i[1])