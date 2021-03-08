from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def move(board, dx, dy):
    new_board = [r[:] for r in board]
    for i in range(N):
        if dx == 1 or dy == 1:
            cur_i = N-1
        else:
            cur_i = 0

        new_row = [0] * N
        new_i = cur_i
        while 0 <= cur_i < N:
            if dx != 0:  # 위아래 (i +- 1)
                if board[cur_i][i] != 0:
                    if board[cur_i][i] == new_row[new_i]:
                        new_row[new_i] += board[cur_i][i]
                        new_i -= dx
                    elif new_row[new_i] == 0:
                        new_row[new_i] = board[cur_i][i]
                    else:
                        new_i -= dx
                        new_row[new_i] = board[cur_i][i]
                cur_i -= dx
                for j in range(N):
                    new_board[j][i] = new_row[j]
            else:  # 좌우 (j +- 1)
                if board[i][cur_i] != 0:
                    if board[i][cur_i] == new_row[new_i]:
                        new_row[new_i] += board[i][cur_i]
                        new_i -= dy
                    elif new_row[new_i] == 0:
                        new_row[new_i] = board[i][cur_i]
                    else:
                        new_i -= dy
                        new_row[new_i] = board[i][cur_i]
                cur_i -= dy
                new_board[i] = new_row
    return new_board

queue = deque()
queue.append((board, 0))

ret = []

while queue:
    board, count = queue.popleft()
    if count == 5:
        ret.append(max([max(r) for r in board]))
        continue
    for dx, dy in directions:
        queue.append((move(board, dx, dy), count+1))

print(max(ret))