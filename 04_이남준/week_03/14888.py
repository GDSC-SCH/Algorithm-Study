import sys

N = int(input())
num_list = list(map(int, sys.stdin.readline().split())) # N개의 수열
operator_list = list(map(int, sys.stdin.readline().split())) # N-1개의 연산자

MAX_MIN = 10000000001

# max, min initialize
max_r = -MAX_MIN
min_r = MAX_MIN

def dfs(plus: int, minus: int, multiply: int, divide: int, count: int, result: int):
    if count == N: # 다 계산되었을 때
        global max_r, min_r
        max_r = max(max_r, result) # 현재 계산된 값과 초기 max값 비교
        min_r = min(min_r, result) # 현재 계산된 값과 초기 min값 비교

    # 연산자 하나씩 줄이면서 dfs 탐색
    if plus > 0:
        dfs(plus - 1, minus, multiply, divide, count + 1, result + num_list[count])
    if minus > 0:
        dfs(plus, minus - 1, multiply, divide, count + 1, result - num_list[count])
    if multiply > 0:
        dfs(plus, minus, multiply - 1, divide, count + 1, result * num_list[count])
    if divide > 0:
        dfs(plus, minus, multiply, divide - 1, count + 1, int(result / num_list[count]))

dfs(operator_list[0], operator_list[1], operator_list[2], operator_list[3], 1, num_list[0])
print(max_r)
print(min_r)