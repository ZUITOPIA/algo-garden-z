n = int(input())
arr = [int(x) for x in input().split()]

dp = [1] * n  # 모든 요소를 1로 초기화 (각 자리마다의 길이 저장)

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# 모든 가능한 증가 부분 수열을 고려해야 하므로