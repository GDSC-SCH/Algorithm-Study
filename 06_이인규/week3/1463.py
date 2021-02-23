import math

lst = []
N =int(input())

x_range = int(math.log(N,3)+1)
y_range = int(math.log(N,2)+1)

for x in range(x_range):
    for y in range(y_range):
        toss = 3**x * 2**y
        if toss <= N:
            lst.append(N-toss+x+y)

print(min(lst))