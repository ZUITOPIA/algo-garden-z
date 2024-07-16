import sys

n = int(sys.stdin.readline())
s = set()

for _ in range(n):
    command = sys.stdin.readline().strip().split()

    if len(command) == 1:
        if command[0] == "all":
            s = set([i for i in range(1,21)])
        else:
            s = set()
    else:
        x = int(command[1])
        if command[0] == "add":
            s.add(x)
        elif command[0] == "check":
            print(1 if x in s else 0)
        elif command[0] == "remove":
            s.discard(x)
        elif command[0] == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)
