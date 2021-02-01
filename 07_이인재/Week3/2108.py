user_input = int(input())

arr = []

for i in range(user_input):
    n = int(input())
    arr.append(n)
     
#산술 평균
print(int(sum(arr)/user_input))

#중앙값
for k in range(user_input):
    q = user_input - k
    for p in range(1, q):
        if arr[p-1] >= arr[p]:
            temp = arr[p-1]
            arr[p-1] = arr[p]
            arr[p] = temp

print(arr[int(user_input/2)])


#최빈값
most_cnt = arr[0]
for j in arr:
    if most_cnt < arr.count(j):
        most_cnt = j

print(most_cnt)

#범위
print(arr[-1] - arr[0])
