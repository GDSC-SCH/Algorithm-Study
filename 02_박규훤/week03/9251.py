s1 = input()
s2 = input()
len1 = len(s1)
len2 = len(s2)

mat = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(len1):
    for j in range(len2):
        if s1[i] == s2[j]:
            mat[i+1][j+1] = mat[i][j] + 1
        else:
            mat[i+1][j+1] = max(mat[i][j+1], mat[i+1][j])

print(mat[-1][-1])