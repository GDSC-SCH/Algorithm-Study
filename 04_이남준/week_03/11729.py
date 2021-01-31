def hanoi(N, start, to, via, list):
    if N == 1:
        list.append((start, to))
    else:
        hanoi(N-1, start, via, to, list)
        list.append((start, to))
        hanoi(N-1, via, to, start, list)

N = int(input())
hanoi_list = []
hanoi(N, 1, 3, 2, hanoi_list)

print(len(hanoi_list))
for i in hanoi_list:
    print(i[0], i[1])