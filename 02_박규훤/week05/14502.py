from collections import deque

N, M = map(int, input().split())
init_lab = [list(map(int, input().split())) for _ in range(N)]

empty = []
init_virus = deque()
for i, row in enumerate(init_lab):
    for j, col in enumerate(row):
        if col == 0:
            empty.append((i, j))
        if col == 2:
            init_virus.append((i, j))

walls = []
for i in range(len(empty)-2):
    for j in range(i+1, len(empty)-1):
        for k in range(j+1, len(empty)):
            walls.append((empty[i], empty[j], empty[k]))

ret = 0
for wall in walls:
    lab = [row[:] for row in init_lab]
    for i, j in wall:
        lab[i][j] = 1
    virus = init_virus.copy()
    while virus:
        i, j = virus.popleft()
        if i > 0 and lab[i-1][j] == 0:
            lab[i-1][j] = 2
            virus.append((i-1, j))
        if i < N-1 and lab[i+1][j] == 0:
            lab[i+1][j] = 2
            virus.append((i+1, j))
        if j > 0 and lab[i][j-1] == 0:
            lab[i][j-1] = 2
            virus.append((i, j-1))
        if j < M-1 and lab[i][j+1] == 0:
            lab[i][j+1] = 2
            virus.append((i, j+1))
    ret = max(ret, sum([row.count(0) for row in lab]))

print(ret)