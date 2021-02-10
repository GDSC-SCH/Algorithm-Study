N = int(input())
nums = [int(x) for x in input().split()]
nums.sort()

M = int(input())
targets = [int(x) for x in input().split()]

for t in targets:
    start, end = 0, N
    contains = False
    while True:
        if end == start:
            break
        mid = (end + start) // 2
        if nums[mid] == t:
            contains = True
            break
        if t < nums[mid]:
            end = mid
        else:
            start = mid + 1
    print(1 if contains else 0)