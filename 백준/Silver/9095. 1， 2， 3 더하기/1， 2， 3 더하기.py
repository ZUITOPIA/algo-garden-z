# 1,2,3을 모두 사용할 필요X
# 1,2,3을 꼭 한 번씩만 사용할 필요X

n = int(input())

arr = [0]*11

arr[1], arr[2], arr[3] = 1, 2, 4  # 직접 나타내보았을 때 알게 된 값들

for i in range(4, len(arr)):
    arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

for _ in range(n):
    n = int(input())
    print(arr[n])