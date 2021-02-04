N, M = map(int, input().split())

nums = [[str(i+1)] for i in range(N)] 
new = nums[:]

for _ in range(M-1):
    old = new
    new = []
    for o in old:
        for n in nums:
            new.append(o + n)

for n in new:
    print(' '.join(n))