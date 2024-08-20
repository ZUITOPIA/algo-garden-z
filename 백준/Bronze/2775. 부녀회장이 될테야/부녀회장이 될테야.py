max_k, max_n = 14, 14

arr = [[0] * (max_n + 1) for _ in range(max_n + 1)]

for i in range(1, max_n+1):
    arr[0][i] = i

for i in range(1, max_k+1):
    for j in range(1, max_n+1):
        arr[i][j] = arr[i][j-1] + arr[i-1][j]

testcase = int(input())
for _ in range(testcase):
    k = int(input())
    n = int(input())
    print(arr[k][n])


# 2층 4호 => 1층의 1호부터 4호까지의 합

# arr[0][1]=1  arr[0][2]=2  arr[0][3]=3
# arr[1][1]=1  arr[1][2]=3  arr[1][3]=6
# arr[2][1]=1  arr[2][2]=4  arr[2][3]=10