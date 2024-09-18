import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    command = list(input().split())

    if command[0] == '1':
        arr.append(command[1])
    elif command[0] == '2':
        if arr:
            print(arr.pop())
        else:
            print(-1)
    elif command[0] == '3':
        print(len(arr))
    elif command[0] == '4':
        print(1 if not arr else 0)
    elif command[0] == '5':
        print(arr[-1] if arr else -1)
