# 몇 번을 봐도 모르겠다... 일단 통과

def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, to_pos)
        return
    hanoi(n - 1, from_pos, aux_pos, to_pos)
    print(from_pos, to_pos)
    hanoi(n - 1, aux_pos, to_pos, from_pos)

a = int(input())

print(2**a-1)
hanoi(a,1,3,2)