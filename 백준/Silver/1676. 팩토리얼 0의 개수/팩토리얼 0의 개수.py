from math import factorial

n = int(input())
count = 0

for value in str(factorial(n))[::-1]:
    if value != "0":
        break
    else:
        count += 1

print(count)