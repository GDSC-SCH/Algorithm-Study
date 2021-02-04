data = [int(i) for i in input().split()]
print(min(data[0], data[1], data[2] - data[0], data[3] - data[1]))