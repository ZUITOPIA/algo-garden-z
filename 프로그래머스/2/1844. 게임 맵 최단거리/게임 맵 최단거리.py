from collections import deque

def bfs(maps, x, y):  
    q = deque()
    q.append([x,y])
    
    r = len(maps) # 행 크기
    c = len(maps[0]) # 열 크기
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    
    while q:
        x, y = q.popleft() # 2차원 배열
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] != 0:
                if maps[nx][ny] == 1:
                    maps[nx][ny] += maps[x][y]
                    q.append([nx,ny])
                    
    return maps[-1][-1] if maps[-1][-1] > 1 else -1 

def solution(maps):
    return bfs(maps,0,0)

    