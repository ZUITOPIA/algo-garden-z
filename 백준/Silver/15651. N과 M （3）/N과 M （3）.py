n, m = map(int, input().split())
arr = []   # 순열 넣어둘 배

def back():
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(1, n+1):
        arr.append(i)
        back()
        arr.pop()

back()