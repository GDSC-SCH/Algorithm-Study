user_input = int(input())

arr = []
result = []

for i in range(user_input):
    arr.append(list(map(int, input().split(" "))))

for j in range(user_input):
    cnt = 1
    tmp = arr[j]

    for k in range(user_input):    
        if tmp[0] < arr[k][0] and tmp[1] < arr[k][1]:
            cnt += 1
    result.append(cnt)

for q in range (user_input):
    print(result[q], end = ' ')