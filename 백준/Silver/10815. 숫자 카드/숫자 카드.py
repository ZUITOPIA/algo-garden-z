n = int(input().strip())
default_arr = set(map(int, input().strip().split()))

m = int(input().strip())
confirmCards = list(map(int, input().strip().split()))

answerArr = []

for i in confirmCards:
    if i in default_arr:
        answerArr.append(1)
    else:
        answerArr.append(0)

# 결과 출력
print(' '.join(map(str, answerArr)))