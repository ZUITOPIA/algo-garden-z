n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(0, i+1):
        if j == 0:  # 다음 행으로 넘어갔을 때
            arr[i][0] += arr[i-1][0]  # 이전 행의 맨 앞, 지금 행의 맨 앞 끼리 더하기
        elif j == i:  # 맨 마지막 열까지 왔을 때
            arr[i][j] += arr[i-1][j-1]  # 이전 행의 맨 뒤, 지금 행의 맨 뒤 끼리 더하기
        else:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])


print(max(arr[n-1]))   # 행이 n-1일 때 가장 마지막 행의 열들 중 가장 큰 값 