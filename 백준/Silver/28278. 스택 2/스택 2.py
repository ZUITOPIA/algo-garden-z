import sys
input = sys.stdin.readline

n = int(input().strip())
arr = []

for _ in range(n):
    command = list(input().split())
    cmd = int(command[0])
    
    if cmd == 1:
        arr.append(command[1])
    elif cmd == 2:
        if arr:
            print(arr.pop())
        else:
            print(-1)
    elif cmd == 3:
        print(len(arr))
    elif cmd == 4:
        print(1 if not arr else 0)
    elif cmd == 5:
        print(arr[-1] if arr else -1)
