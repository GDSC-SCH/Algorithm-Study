# 꼭 이분탐색... 빅O 문제?

n = int(int(input()))
lst = list(map(int,input().split()))
X = int(int(input()))

lst.sort()
start = 0
end = n-1
cnt = 0

while start != end:
    num = lst[start] + lst[end]

    if num == X:
        cnt += 1
        start += 1
    elif num > X:
        end -= 1
    else:
        start += 1

print(cnt)