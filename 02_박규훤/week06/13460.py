from collections import deque

N, M = map(int, input().split())
directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
visit = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
board = [list(input()) for _ in range(N)]
for i in range(N):
    for j, c in enumerate(board[i]):
        if c == 'R':
            red_i, red_j = i, j
        elif c == 'B':
            blue_i, blue_j = i, j

def move(i, j, dx, dy):
    dist = 0
    while board[i+dx][j+dy] != '#' and board[i][j] != 'O':
        i += dx
        j += dy
        dist += 1
    return i, j, dist

queue = deque()
# 시작점. 로직이 이동 후 그대로 출력이므로 이동 횟수 1
queue.append((red_i, red_j, blue_i, blue_j, 1))
visit[red_i][red_j][blue_i][blue_j] = True

def tilt():
    while queue:
        red_i, red_j, blue_i, blue_j, count = queue.popleft()
        if count > 10:
            break
        for dx, dy in directions:
            # dx, dy 방향으로 이동 후 위치 구하기
            new_red_i, new_red_j, red_dist = move(red_i, red_j, dx, dy)
            new_blue_i, new_blue_j, blue_dist = move(blue_i, blue_j, dx, dy)
            if board[new_blue_i][new_blue_j] != 'O':
                if board[new_red_i][new_red_j] == 'O':
                    print(count)
                    return
                # 겹쳐지면 더 먼 곳에서 온 구슬이 한 칸 뒤로
                if new_red_i == new_blue_i and new_red_j == new_blue_j:
                    if red_dist > blue_dist:
                        new_red_i -= dx
                        new_red_j -= dy
                    else:
                        new_blue_i -= dx
                        new_blue_j -= dy
                # 같은 자리에서 출발하는 경우 해본 적 있는지 확인
                if not visit[new_red_i][new_red_j][new_blue_i][new_blue_j]:
                    visit[new_red_i][new_red_j][new_blue_i][new_blue_j] = True
                    queue.append((new_red_i, new_red_j, new_blue_i, new_blue_j, count+1))
    print(-1)

tilt()