n, m = map(int, input().split())     # 입력 값 n과 m
array = [list(input().strip()) for _ in range(n)]  # 각 줄을 리스트로 변환하여 2차원 리스트 생성

a = ["WBWBWBWB", "BWBWBWBW"] * 4
b = ["BWBWBWBW", "WBWBWBWB"] * 4

min_count = float('inf')

for i in range(n-7):     # 입력받은 크기에서 -> 8*8크기의 체스판으로 만들려고 한다
    for j in range(m-7):
        w_start_count = 0  # 맨 처음이 w로 시작하는 경우의 count
        b_start_count = 0  # 맨 처음이 b로 시작하는 경우의 count

        for x in range(8):  # 한 번에 8칸 확인씩
            for y in range(8):
                if array[i+x][j+y] == a[x][y]:
                    w_start_count += 1
                if array[i+x][j+y] == b[x][y]:
                    b_start_count += 1
        min_count = min(min_count, w_start_count, b_start_count)  # 최소 값 비교


print(min_count)