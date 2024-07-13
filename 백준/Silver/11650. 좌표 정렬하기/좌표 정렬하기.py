n = int(input())
arr = []

for i in range(n):
    [x, y] = map(int, input().split())
    arr.append([x,y])

# arr.sort()  대신 sorted를 사용하려면 아래와 같이 사용
array = sorted(arr)

for i in array:
    print(i[0], i[1])