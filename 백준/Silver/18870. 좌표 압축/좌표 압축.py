n = int(input())
values = list(map(int, input().split()))

arr = sorted(list(set(values)))

dic = {}

for i in range(len(arr)):
    dic[arr[i]] = i  # 값과 인덱스 매칭시켜 저장해두기

for i in values:
    print(dic[i], end=" ")