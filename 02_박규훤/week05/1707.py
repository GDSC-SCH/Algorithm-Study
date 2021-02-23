import sys
from collections import deque

input = sys.stdin.readline

C = int(input())

for _ in range(C):
    n_v, n_e = list(map(int, input().split()))
    edges = [[] for _ in range(n_v+1)]
    for _ in range(n_e):
        s, e = [int(x) for x in input().split()]
        edges[s].append(e)
        edges[e].append(s)
    visit = [0] * (n_v+1)

    stop = False
    for i in range(1, n_v+1):
        if stop:
            break
        if visit[i] > 0:
            continue

        visit[i] = 1
        queue = deque([i])

        while queue and not stop:
            q = queue.popleft()
            c = 3 - visit[q]

            for p in edges[q]:
                # q와 연결된 노드가 분류되지 않았으면 q의 반대로 분류
                if visit[p] == 0:
                    visit[p] = c
                    queue.append(p)
                elif visit[p] == visit[q]:
                    stop = True
                    break
    print('YES' if not stop else 'NO')