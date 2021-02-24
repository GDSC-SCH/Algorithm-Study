# 버리긴 아까운것...
# import sys

# lst = []

# def make_one(num,cnt):

#     if num == 1:
#         lst.append(cnt)
#         return

#     if cnt == min(lst)-1:
#         return

#     if num % 3 == 0:
#         make_one(num//3,cnt+1)
    
#     if num % 2 == 0:
#         make_one(num//2,cnt+1)
    
#     if cnt < min(lst):
#         make_one(num-1,cnt+1)

# num = int(sys.stdin.readline())

# lst.append(num//3+num%3)
# make_one(num,0)
# print(min(lst))

import sys

num = int(sys.stdin.readline())

lst = [0,1,1,2,3]

for i in range(6,num+1):
    lst.append(0)

    lst[i-1] = lst[i-2] + 1

    if i % 3 == 0 and lst[i-1] > lst[i//3-1] + 1:
        lst[i-1] = lst[i//3-1] + 1
    
    if i % 2 == 0 and lst[i-1] > lst[i//2-1] + 1:
        lst[i-1] = lst[i//2-1] + 1

print(lst[num-1])