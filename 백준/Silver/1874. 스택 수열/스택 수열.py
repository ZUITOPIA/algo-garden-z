n = int(input())
stack = []
arr = []
start = 1
for i in range(n):
    num = int(input())
    while start <= num:
        stack.append(start)
        arr.append("+")
        start += 1

    if stack[-1] == num:  # 가장 최근에 들어온 값
        stack.pop()
        arr.append("-")
    else:
        print("NO")
        exit()

for i in arr:
    print(i)