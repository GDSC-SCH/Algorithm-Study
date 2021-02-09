num = int(input())

print_list=[]

for _ in range(num):
    N, M = map(int,input().split())

    imp = list(map(int,input().split()))
    index = [0 for _ in range(N)] 
    index[M] = 1 

    count=0
    while True:
        if imp[0] == max(imp): # 맨 앞 위치값과 비교
            count+=1

            if index[0] != 1: 
                del imp[0]
                del index[0]
            else:
                print_list.append(count)
                break
        else:
            imp.append(imp[0])
            index.append(index[0])
            del imp[0]
            del index[0]

for i in range(len(print_list)):
    print(print_list[i])