n_point, n_edge, start = [int(x) for x in input().split()]

edges = [[0] * (n_point+1) for _ in range(n_point+1)]
for _ in range(n_edge):
    s, e = [int(x) for x in input().split()]
    edges[s][e] = 1
    edges[e][s] = 1
visit = [0] * (n_point+1)

dfs_result = []
def dfs(point):
    dfs_result.append(point)
    visit[point] = 1
    for p in range(1, n_point+1):
        if visit[p] == 0 and edges[point][p] == 1:
            dfs(p)

# dfs에서 visit의 값을 모두 1로 변경했으므로 bfs에서는 반대로.
# 큐를 이용하여 방문한 순서대로 나중에 순회를 할 수 있도록.
bfs_result = []
def bfs(point):
    queue = [point]
    visit[point] = 0
    while queue:
        point = queue.pop(0)
        bfs_result.append(point)
        for p in range(1, n_point+1):
            if visit[p] == 1 and edges[point][p] == 1:
                queue.append(p)
                visit[p] = 0

dfs(start)
bfs(start)
print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))