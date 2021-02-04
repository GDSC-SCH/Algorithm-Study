word = input().upper()
chars = list(set(word))
nums = [word.count(c) for c in chars]
sorted_num = sorted(nums, reverse=True)
if len(nums) >= 2 and sorted_num[0] == sorted_num[1]:
    print('?')
else:
    print(chars[nums.index(max(nums))])