n = int(input())
countArr = [0, 1, 2]

for i in range(3, n+1):
    countArr.append(countArr[i-1] + countArr[i-2])

print(countArr[n] % 10007) # 출력 조건 : 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.