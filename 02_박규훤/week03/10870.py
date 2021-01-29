n = int(input())

p1, p2 = 0, 1

for _ in range(n):
    p1, p2 = p2, p1+p2
print(p1)