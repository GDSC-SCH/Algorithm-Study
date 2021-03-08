N = int(input())

row = [0] * N  # 열에서 퀸 존재 여부
diag1 = [0] * (2*N-1)  # 오른쪽 대각선에서 퀸 존재 여부
diag2 = [0] * (2*N-1)  # 왼쪽 대각선에서 퀸 존재 여부

ret = 0
def place(r):
    global ret
    if r == N:
        ret += 1
        return
    for c in range(N):
        if row[c] + diag1[r+c] + diag2[N-1+r-c] == 0:
            row[c] = diag1[r+c] = diag2[N-1+r-c] = 1
            place(r+1)
            row[c] = diag1[r+c] = diag2[N-1+r-c] = 0

place(0)
print(ret)