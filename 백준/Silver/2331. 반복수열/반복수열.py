a, p = map(int, input().split())
result_arr = []  # 결과 반환하기 위한 배열


def makeNum(v):
    if v in result_arr:
        return result_arr.index(v)  # 이미 있는 값일 때, 그 값의 인덱스를 찾아 반환하기 (반복수열의 시작인덱스)
    result_arr.append(v)
    next_value = sum(int(digit) ** p for digit in str(v))
    return makeNum(next_value)

arr_length = makeNum(a)  # 반복 수열을 제외한 갯수

print(arr_length)
