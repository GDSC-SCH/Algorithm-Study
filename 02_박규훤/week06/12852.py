N = int(input())

count = [100000] * (N+1)
count[1] = 0
past = [0] * (N+1)

for i in range(1, N+1):
    if i*3 <= N and count[i*3] > count[i]+1:
        count[i*3] = count[i] + 1
        past[i*3] = i
    if i*2 <= N and count[i*2] > count[i]+1:
        count[i*2] = count[i] + 1
        past[i*2] = i
    if i+1 <= N and count[i+1] > count[i]+1:
        count[i+1] = count[i] + 1
        past[i+1] = i

print(count[N])
while True:
    print(N, end=' ')
    if N == 1:
        break
    N = past[N]