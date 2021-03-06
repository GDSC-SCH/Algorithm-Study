from heapq import heappush, heappop

n = int(input())
m = int(input())
node = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    node[a].append([b, c])

# 1753 -> 이중리스트
dp = [[1e9]*(n+1) for _ in range(n+1)]
heap = [[] for _ in range(n+1)]

for i in range(1, n+1): # 출발
    dp[i][i] = 0
    heappush(heap[i], [0, i])
    while heap[i]:
        w, n = heappop(heap[i])
        for n_n, wei in node[n]:
            n_w = wei + w
            if n_w < dp[i][n_n]:
                dp[i][n_n] = n_w
                heappush(heap[i], [n_w, n_n])
            
for i in dp[1:]:
    for j in i[1:]:
        if j == 1e9:
            print(0, end = ' ')
        else:
            print(j, end = ' ')
    print()