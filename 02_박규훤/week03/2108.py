import sys
from collections import Counter

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]
# nums = [int(randint(-4000, 4000)) for _ in range(N)]

print(round(sum(nums)/N))

nums.sort()
print(nums[N//2])

counter = Counter(nums)
most_comm = counter.most_common()
if len(most_comm) == 1:
    print(most_comm[0][0])
elif most_comm[0][1] == most_comm[1][1]:
    print(most_comm[1][0])
else:
    print(most_comm[0][0])

print(max(nums) - min(nums))