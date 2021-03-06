from heapq import heappush, heappop

INF = 1e9

V, E = map(int, input().split())
K = int(input())
node = [[] for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int, input().split())
    node[u].append([v, w])
    
dp = [INF] * (V+1) 
heap = []

def dijkstra(start):
    dp[start] = 0
    heappush(heap, [0, start]) # heap에 [0, start] 추가 (이중리스트)
    while heap:
        w, n = heappop(heap) # 제일 작은 원소 삭제 후 리턴 (이중리스트라서 값 2개 받음)
        for n_n, wei in node[n]: 
            n_w = wei + w # 새로운 노드를 거쳐서 갔을때 이동거리 
            if n_w < dp[n_n]: # 기존 이동거리보다 작으면 업데이트
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])
                
dijkstra(K)

for i in dp[1:]:
    print(i if i!= INF else 'INF')