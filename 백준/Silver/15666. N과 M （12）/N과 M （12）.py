n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

arr = []  # 결과 담을 배열

def dfs(start):
    if len(arr) == m:
        print(*arr)  # temp 리스트의 요소들을 공백으로 구분하여 출력
        return
    prev = 0
    for i in range(start, n):
        if prev != nums[i]:
            arr.append(nums[i])
            prev = nums[i]
            dfs(i)
            arr.pop()

dfs(0)
