C = int(input())

for _ in range(C):
    scores = [int(x) for x in input().split()][1:]
    n = len(scores)
    mean = sum(scores) / n
    over = [s for s in scores if s > mean]
    print('%.3f%%' %round(len(over) / n * 100, 3))