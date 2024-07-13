n = int(input())
cnt = 0
result = 666  # 첫번째 666을 포함한 숫자를 찾기 위해 초기값을 666으로 설정

while True:
    if "666" in str(result):
        cnt += 1
    if cnt == n:
        break
    result += 1
print(result)