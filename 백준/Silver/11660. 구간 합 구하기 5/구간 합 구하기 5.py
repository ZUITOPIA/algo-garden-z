import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

prefix = [[0] * (len(arr[0]) + 1) for _ in range(n + 1)] # 누적 합 배열 생성

for i in range(1, n + 1):
    for j in range(1, len(arr[0]) + 1):
        prefix[i][j] = arr[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]  # 누적 합 계산

sum_arr = []
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    total_sum = (prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1])
    sum_arr.append(total_sum)

for result in sum_arr:
    print(result)
