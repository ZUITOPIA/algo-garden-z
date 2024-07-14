n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

arr = list(set(arr))  # 중복 제거
arr.sort()  # 알파벳 순서대로 정렬
arr.sort(key=len)  # 개수 크기대로 정렬

for i in arr:
    print(i)