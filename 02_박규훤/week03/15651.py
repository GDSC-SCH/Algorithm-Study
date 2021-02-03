N, M = [int(x) for x in input().split()]
nums = [[str(n)] for n in range(1, N+1)]
new = nums[:]

m = 1
while m != M:
    old = new
    new = []
    for o in old:
        for n in nums:
            new.append(o+n)
    m += 1

for n in new:
    print(' '.join(n))