# n : 데이터의 크기
n = int(input())

# plus : 양수 데이터 리스트, minus : 음수 데이터 리스트
plus = []
minus = []

result = 0
for i in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num <= 0:
        minus.append(num)
    else:
        result += num

# 정렬
plus.sort(reverse=True)
minus.sort()  # ex) -3 -2 -1

# 양수 묶기
while len(plus) > 1:
    result += plus.pop(0) * plus.pop(0)

# 리스트에 양수가 하나 남은 경우
if plus:
    result += plus[0]

# 음수 묶기
while len(minus) > 1:
    result += minus.pop(0) * minus.pop(0)

# 음수가 하나 남은 경우
if minus:
    result += minus[0]

print(result)
