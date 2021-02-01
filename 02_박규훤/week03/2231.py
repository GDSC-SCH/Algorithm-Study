N = int(input())

gen = [0] * (N+1)

for i in range(1, N+1):
    g = i + sum([int(s) for s in str(i)])
    if g <= N:
        if gen[g] == 0 or gen[g] > i:
            gen[g] = i

print(gen[N])