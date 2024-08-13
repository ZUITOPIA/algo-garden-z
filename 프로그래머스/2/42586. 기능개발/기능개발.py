from collections import deque

def solution(progress, speeds):
    answer = []
    days = deque()  # 각 progress의 원소마다 완료하기까지 필요한 날짜 수 배열

    for i in range(len(progress)):    # progress 원소마다 배포까지 얼마나 걸리는지 확인하기 위해 
        x = (100 - progress[i]) / speeds[i] 

        if x == int(x):
            days.append(int(x))
        else:
            days.append(int(x)+1) # 딱 떨어지지 않았다면 = 나머지가 있었다면 => 하루 더 밀리게 되므로 +1

    while days:  # 남은 날짜 배열이 존재하는 동안
        temp = days.popleft() 
        count = 1  # 원소 값 빼내었으니 count up
        
        while days and temp >= days[0]:  # 앞 인덱스가 다음 인덱스의 원소보다 같거나 크다면 같이 배포할 수 있는 것이므로
            days.popleft()
            count += 1 # count up
        answer.append(count) # 각 요일마다 몇 개씩 배포하는지 들어있는 배열

    return answer