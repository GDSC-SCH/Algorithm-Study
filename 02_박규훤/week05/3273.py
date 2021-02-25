import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

target = int(input())

answer = []

for num in nums:
    if target - num in nums and num not in answer and num * 2 != target:
        answer.append(num)
        answer.append(target-num)

print(len(answer)//2)