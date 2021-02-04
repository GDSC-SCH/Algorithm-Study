A = [True] + [False for _ in range(10000)]
i = c = 1
while c <= 10000:
    temp = [int(s) for s in str(i)]
    i = i + sum(temp)
    while i <= 10000:
        if A[i]:
            break
        A[i] = True
        temp = [int(s) for s in str(i)]
        i = i + sum(temp)
    c += 1
    i = c

for i, a in enumerate(A):
    if not a:
        print(i)