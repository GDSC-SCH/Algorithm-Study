import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

cut_low = 0
cut_high = max(trees)
result = 0
while cut_high >= cut_low:
    pivot = int((cut_low + cut_high) / 2)
    # 나무의 총 길이 계산
    cut_tree = sum([x - pivot if x >= pivot else 0 for x in trees])
    
    # 비교하기
    if cut_tree >= M:
        cut_low = pivot + 1
       
        if result < pivot: result = pivot
    elif cut_tree < M: cut_high = pivot - 1

print(result)