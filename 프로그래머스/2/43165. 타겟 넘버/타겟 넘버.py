def solution(numbers, target):
    answer = 0 # 타겟 넘버를 만드는 모든 경우의 수

    # 재귀를 통해 모든 경우 수 구하기
    def recursion(n, sum):
        nonlocal answer
        
        # 1 종료 조건 (모든 배열의 원소를 다 사용하면서 합계가 target과 같을 때)
        if (len(numbers) == n):
            if (target == sum):
                answer += 1  # answer 증가 -> 모든 숫자에 대해서 돌고, 합계가 타겟과 같을 경우
            return

        # 2 유도 부분(재귀하는 부분)
        # 2-1. 배열의 값을 모두 다 더한다.
        # 2-2. 이번에도 종료조건에 만족하지않으면 뒤에부터 하나씩 빼기
        recursion(n + 1, sum + numbers[n])
        recursion(n + 1, sum - numbers[n])

    recursion(0, 0)  # 몇 개의 수를 사용했는지, n개까지의 합

    return answer