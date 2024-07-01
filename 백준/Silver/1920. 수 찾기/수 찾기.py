N = int(input())  # 첫째줄 입력
defaultSet = set(map(int, input().split()))  # 리스트를 집합으로 변환

M = int(input())  # 둘째줄 입력
inputList = list(map(int, input().split()))

for num in inputList:
    if num in defaultSet:
        print(1)
    else:
        print(0)
