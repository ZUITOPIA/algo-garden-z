import sys

arr = []

n = int(input())

for _ in range(n):
    request = sys.stdin.readline().rstrip()
    temp = request.split(" ")

    if temp[0] == "push_back":
        arr.append(int(temp[1]))
    elif temp[0] == "push_front":
        arr.insert(0, int(temp[1]))
    elif temp[0] == "pop_front":
        if len(arr) != 0:
            print(arr.pop(0))
        else:
            print(-1)
    elif temp[0] == "pop_back":
        if len(arr) != 0:
            print(arr.pop(-1))
        else:
            print(-1)
    elif temp[0] == "size":
        print(len(arr))
    elif temp[0] == "empty":
        if len(arr) != 0:
            print(0)
        else:
            print(1)
    elif temp[0] == "front":
        if len(arr) != 0:
            print(arr[0])
        else:
            print(-1)
    elif temp[0] == "back":
        if len(arr) != 0:
            print(arr[-1])
        else:
            print(-1)
    else:
        break
