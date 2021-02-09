import sys

N, M = map(int, sys.stdin.readline().split())

depth_list = [1 for i in range(M)]

def dfs(depth: int):
    if depth == M:
        for i in range(M):
            print(depth_list[i], end=" ")
        print()
        return
    for i in range(1, N+1):
        depth_list[depth] = i
        dfs(depth + 1)

dfs(0)