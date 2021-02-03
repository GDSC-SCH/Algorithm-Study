def dfs(cnt, result, p, m, mul, div):
    global max_result
    global min_result
    if cnt == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    if p:
        dfs(cnt+1, result + nums[cnt], p-1, m, mul, div)
    if m:
        dfs(cnt+1, result - nums[cnt], p, m-1, mul, div)
    if mul:
        dfs(cnt+1, result * nums[cnt], p, m, mul-1, div)
    if div:
        dfs(cnt+1, -(-result // nums[cnt]) if result < 0 else result // nums[cnt], p, m, mul, div-1)

n = int(input())
nums = list([int(x) for x in input().split()])
opers = list([int(x) for x in input().split()])
max_result = -1000000001
min_result = 1000000001
dfs(1, nums[0], opers[0], opers[1], opers[2], opers[3])
print(max_result)
print(min_result)