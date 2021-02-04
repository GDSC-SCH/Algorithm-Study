nums = [i+1 for i in range(10000)]

self_number = []
for i in nums:
    number = i
    for j in str(i):
        number += int(j)
    self_number.append(number)

self_number = set(self_number)

for n in nums:
    if n not in self_number:
        print(n)