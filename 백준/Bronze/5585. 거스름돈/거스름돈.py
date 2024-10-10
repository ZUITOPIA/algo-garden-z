n = int(input())
arr = [500, 100, 50, 10, 5, 1]

money = 1000 - n

count = 0

for i in arr:
    count += money // i
    money %= i

print(count)