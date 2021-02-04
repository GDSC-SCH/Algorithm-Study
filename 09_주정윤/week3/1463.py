n = int(input())

result_list = [0 for _ in range(x+1)]

for i in range(1, x+1):
    if i==1:
        result[i]=0
        continue
    result_list[i] = result_list[i-1]+1

    if i%3==0 and result_list[i//3]+1<result_list[i]:
        result_list[i]=result_list[i//3]+1
    elif i%2==0 and result_list[i//2]+1<result_list[i]:
        result_list[i] = result_list[i//2]+1

print(result_list[n])