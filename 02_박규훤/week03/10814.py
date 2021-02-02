N = int(input())
names = []
ages = []
for _ in range(N):
    inp = input().split()
    ages.append(int(inp[0]))
    names.append(inp[1])

idx = []
for age in sorted(set(ages)):
    idx.extend([i for i, a in enumerate(ages) if a == age])

for i in idx:
    print(ages[i], names[i])