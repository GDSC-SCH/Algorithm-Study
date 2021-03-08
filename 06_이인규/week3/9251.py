one = input()
two = input()

lst = [[0 for _ in range(len(two)+1)] for __ in range(len(one)+1)]

for i in range(1,len(one)+1):
    for j in range(1,len(two)+1):
        if one[i-1] == two[j-1]:
            lst[i][j] = lst[i-1][j-1] + 1
        else:
            lst[i][j] = max(lst[i][j-1], lst[i-1][j])

print(lst[-1][-1])