nums = [int(input()) for _ in range(int(input()))]
idx = 0
stack = []
num = 1
ret = []

no = False
while True:
    if idx == len(nums):
        break
    if num <= nums[idx]:
        stack.append(num)
        ret.append('+')
        num += 1
    elif stack[-1] == nums[idx]:
        ret.append('-')
        stack.pop()
        idx += 1
    else:
        no = True
        break

if no:
    print('NO')
else:
    print('\n'.join(ret))