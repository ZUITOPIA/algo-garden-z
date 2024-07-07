import sys
input = sys.stdin.readline
n = int(input())
num_list = sorted(list(map(int, input().split())))

m = int(input())
m_arr = list(map(int, input().split()))

count = [0]*20000001

for num in num_list:
    count[num + 10000000] += 1

# 결과 출력
result = []
for num in m_arr:
    result.append(count[num + 10000000])

print(' '.join(map(str, result)))