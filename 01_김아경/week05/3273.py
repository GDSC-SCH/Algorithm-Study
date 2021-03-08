n = int(input())
data = list(map(int, input().split()))
x = int(input())

count = 0
data.sort()

end_idx = n-1

for i in range(n):
    start_idx = i
    #end_idx = n-1 # 여기서 end 초기화하면 시간초과,,, 그리고 초기화 필요 없음
    while start_idx < end_idx:
        if data[start_idx] + data[end_idx] == x:
            count += 1
            break
        elif data[start_idx] + data[end_idx] > x:
            end_idx -= 1
        else:
            break

print(count)