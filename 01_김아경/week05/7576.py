from collections import deque

def bfs(q, day):
    count = day
    while q:
        # pop
        v = q.popleft()
        nowX = v[0]
        nowY = v[1]
        count = v[2]
        # 위, 아래, 왼, 오 토마토 익히기
        for i in range(4):
            newX = nowX + dx[i]
            newY = nowY + dy[i]
            if (0 <= newX < N) and (0 <= newY < M): # 토마토가 상자안에 있으면
                if tomato[newX][newY] == 0 and tomato[newX][newY] != -1: 
                # 토마토가 안 익었고 비어있지 않으면
                    tomato[newX][newY] = 1 # 토마토 익히기!!
                    q.append([newX, newY, count + 1]) # 
    return count

def check(day, tomato):
    for i in range(len(tomato)):
        for j in range(len(tomato[i])):
            if tomato[i][j] == 0:
                return -1
    return day

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
day = 0
q = deque([])

for i in range(len(tomato)):
    for j in range(len(tomato[i])):
        if tomato[i][j] == 1:
            q.append([i, j, day])
day = bfs(q, day)

print(check(day, tomato))