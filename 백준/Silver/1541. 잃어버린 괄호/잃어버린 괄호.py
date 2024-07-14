arr = input().split("-")
result = 0

for item in arr[0].split("+"):
    result += int(item)    # 맨 처음 항목은 초기값으로 저장해두는 느낌

for item in arr[1:]:
    for num in item.split("+"): 
        result -= int(num)

print(result)