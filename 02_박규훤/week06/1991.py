N = int(input())
i2w = [chr(65+i) for i in range(N)]
w2i = {chr(65+i): i for i in range(N)}

left = [None] * N
right = [None] * N

for _ in range(N):
    n, l, r = [w2i[w] if w in w2i else None for w in input().split()]
    left[n] = l
    right[n] = r

stack = [0]
queue = [0]
result_f = []
result_m = []
result_b = []

def front(n):
    result_f.append(n)
    if left[n]:
        front(left[n])
    if right[n]:
        front(right[n])

def middle(n):
    if left[n]:
        middle(left[n])
    result_m.append(n)
    if right[n]:
        middle(right[n])

def back(n):
    if left[n]:
        back(left[n])
    if right[n]:
        back(right[n])
    result_b.append(n)

front(0)
middle(0)
back(0)

print(''.join(i2w[i] for i in result_f))
print(''.join(i2w[i] for i in result_m))
print(''.join(i2w[i] for i in result_b))
