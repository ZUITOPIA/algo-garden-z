n = int(input())
arr = list(map(int, input().split()))

arr.sort()

sum = 0
result = 0

for i in range(n):
    sum += arr[i]  # 현재 배열 요소들의 합
    result += sum  # 전체 누적 합

print(result)

# 방법 : 가장 적은 시간을 소요하는 순서대로 정렬한 후, 각 사람의 인출 시간을 누적해서 더해 나가기