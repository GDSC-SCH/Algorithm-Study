from collections import deque

N, M = map(int, input().split())
i, j, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]

# 사면에 청소 안 된 구역이 있는 경우:
#     왼쪽 방향으로 돌아 전진하여 청소
# 모두 청소 됨
#     현재 방향에서 위치 -1

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

room[i][j] = 2
cleaned = 1
all_clean = room[i-1][j] > 0 and room[i+1][j] > 0 and room[i][j-1] > 0 and room[i][j+1] > 0

while not (all_clean and room[i-directions[d][0]][j-directions[d][1]] == 1):
    if all_clean:
        i -= directions[d][0]
        j -= directions[d][1]
    else:
        d = d-1 if d > 0 else 3
        if room[i+directions[d][0]][j+directions[d][1]] == 0:
            i += directions[d][0]
            j += directions[d][1]
            room[i][j] = 2
            cleaned += 1
    all_clean = room[i-1][j] > 0 and room[i+1][j] > 0 and room[i][j-1] > 0 and room[i][j+1] > 0

print(cleaned)