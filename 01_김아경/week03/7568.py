N = int(input())
data = []

for i in range(N):
    data.append([j for j in map(int, input().split())])
     
result = []
for i in range(N):
    x, y = data[i]
    count = 1
    for j in range(N):
        p, q = data[j-1]
        
        if x < p and y < q:
            count += 1
    
    result.append(str(count))

print(" ".join(result))