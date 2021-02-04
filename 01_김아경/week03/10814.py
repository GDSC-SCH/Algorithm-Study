N = int(input())
data = []
for i in range(N):
    a, b = map(str, input().split())
    data.append([int(a), b])
   
data_s = sorted(data, key = lambda data : data[0])

for d in data_s:
    for i in range(2):
        print(d[i], end = ' ')
    print()