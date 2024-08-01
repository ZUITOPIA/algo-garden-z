import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]  # 0번 제외, 1번부터 n번까지
visited = [False]*(n+1)  # 마찬가지로 0번 제외하고 각 노드당 방문확인 배열

count = 0   # 연결 개수

for _ in range(m):   # 간선 개수만큼 노드와 노드 이어붙이기
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)   # 양방향(무방향)

def bfs(start):
    queue = deque([start])  # 시작 노드를 큐에 추가
    visited[start] = True  # 방문한 것으로 처리
    while queue:  # 큐가 비어있지 않을 때
        node = queue.popleft()  # 맨 앞 노드 빼내기
        for i in graph[node]:  # 맨 앞 노드와 연결되어있는 정점들 체크
            if not visited[i]:  # 아직 방문하지 않았다면
                visited[i] = True  # 방문한 것으로 처리
                queue.append(i)  # 큐에 추가함으로써 i 노드 기준 인접한 정점들 탐색이 가능하도록 함


for i in range(1, n+1):   # 인덱스는 1번부터
    if not visited[i]:
        if not graph[i]:  # 연결된 노드가 존재하지 않는 경우
            count += 1
            visited[i] = True
        else:
            bfs(i)  # 연결된 정점이 있으면 방문했다가 오기
            count += 1


print(count)