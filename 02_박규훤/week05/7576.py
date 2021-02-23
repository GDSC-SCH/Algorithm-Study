import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

width, height = list(map(int, input().split()))
grid = []
tomato = deque()

for h in range(height):
    line = list(map(int, input().split()))
    grid.append(line)
    for i, t in enumerate(line):
        if t == 1:
            tomato.append((h, i))

days = -1
while tomato:
    days += 1
    for _ in range(len(tomato)):
        h, w = tomato.popleft()
        for i in range(4):
            x, y = h+dx[i], w+dy[i]
            if 0 <= x < height and 0 <= y < width and grid[x][y] == 0:
                grid[x][y] = 1
                tomato.append([x, y])

ret = days
for l in grid:
    if 0 in l:
        ret = -1
        break

print(ret)