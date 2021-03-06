def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n+1): # index 
        # i : 목적지 / v : 출발지
        if visit[i] == 0 and s[v][i] == 1: # 방문하지 않은 노드 and 인접노드 
            dfs(i)

def bfs(v):
    queue = [v]
    visit[v] = 0
    while(queue):
        # pop
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        # dfs와 동일
        for i in range(1, n+1):
            if visit[i] == 1 and s[v][i] == 1:
                queue.append(i)
                visit[i] = 0

n, m, v = map(int, input().split())
s = [[0] * (n+1) for i in range(n+1)] # 행렬로 인접 노드 확인
visit = [0 for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1
    
dfs(v)
print()
bfs(v)