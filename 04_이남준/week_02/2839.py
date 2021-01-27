# 풀이하지 못함

kg = [5, 3]

N = int(input())

count = 0
for i in kg:
    count += N // i
    N %= i

print(count)