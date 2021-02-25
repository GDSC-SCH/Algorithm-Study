import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
edges = [dict() for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    if v in edges[u]:
        edges[u][v] = min(edges[u][v], w)
    else:
        edges[u][v] = w

for K in range(1, n+1):
    inf = float('inf')
    min_dist = [inf] * (n+1)
    min_dist[K] = 0

    heap = []
    heapq.heappush(heap, (0, K))

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)

        # 최단 경로보다 길면 다른 노드로 가는 경로도 현재의 최단경로로 계산하면 되니까 볼 필요가 없음
        if min_dist[cur_node] < cur_dist:
            continue

        for next_node in edges[cur_node]:
            next_d = cur_dist + edges[cur_node][next_node]
            if next_d < min_dist[next_node]:
                min_dist[next_node] = next_d
                # 최단거리가 업데이트 됐으므로 해당하는 노드들 다시 계산
                heapq.heappush(heap, (next_d, next_node))

    print(' '.join([str(i if i != inf else 0) for i in min_dist[1:]]))
