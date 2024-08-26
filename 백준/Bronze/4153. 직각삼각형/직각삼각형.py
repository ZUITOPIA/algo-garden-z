while True:
    arr = list(map(int, input().split()))
    if sum(arr) == 0:
        break

    arr.sort()
    m = arr.pop()  # 입력받은 수 중에 가장 큰 값

    if arr[0]**2 + arr[1]**2 == m**2:
        print("right")
    else:
        print("wrong")