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

S, E = map(int, input().split())
inf = float('inf')

min_dist = [inf] * (n+1)
min_dist[S] = 0
past = [0] * (n+1)

heap = []
heapq.heappush(heap, (0, S))

while heap:
    cur_dist, cur_node = heapq.heappop(heap)

    if min_dist[cur_node] < cur_dist:
        continue

    for next_node in edges[cur_node]:
        next_d = cur_dist + edges[cur_node][next_node]
        if next_d < min_dist[next_node]:
            min_dist[next_node] = next_d
            past[next_node] = cur_node
            heapq.heappush(heap, (next_d, next_node))

output = [E]
while True:
    output.insert(0, past[output[0]])
    if output[0] == S:
        break

print(min_dist[E])
print(len(output))
print(' '.join(map(str, output)))