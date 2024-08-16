a = int(input())
b = int(input())
c = int(input())

mul_arr = list(str(a*b*c))  # ['1', '7', '0', '3', '7', '3', '0', '0']
arr = [str(i) for i in range(10)]  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

result_arr = [0]*10

for i in mul_arr:
    for j in arr:
        if i == j:
            result_arr[int(j)] += 1
        else:
            result_arr[int(j)] += 0

for i in result_arr:
    print(i)