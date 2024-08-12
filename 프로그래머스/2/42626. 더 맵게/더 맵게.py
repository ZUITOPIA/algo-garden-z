import heapq

def solution(scoville, K):
    answer = 0 # 최소 섞은 횟수
    
    heapq.heapify(scoville) # heap 자료구조 생성

    if(scoville[0] >= K):
        return 0
    
    while(len(scoville) > 1):
        # 1. 스코빌 지수가 가장 낮은 두 개의 음식을 가져온다.
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        
        # 2. 두 음식을 특별한 방법으로 섞는다.
        
        # 3. 섞은 음식을 heap 자료구조에 삽입한다.
        heapq.heappush(scoville, a + (b * 2))
        answer += 1
        
        # 4. 모든 스코빌 지수가 K 이상인지 확인한다.
        if(scoville[0] >= K):
            return answer
    
    return -1