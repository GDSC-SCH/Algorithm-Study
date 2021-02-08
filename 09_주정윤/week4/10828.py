# 명령의 수
N = int(input())

list=[]
num_list=[]
ans_list=[]

for i in range(N):
    list = input().split()

    if list[0] == "push": #명령어가 push일때
        num_list.append(int(list[1]))
    elif list[0] == "top": #명령어가 top일때
        if len(num_list) == 0:
            ans_list.append(-1)
        else:
            ans_list.append(num_list[-1])
        
    elif list[0] == "size": #명령어가 size일때
        ans_list.append(len(num_list))
    elif list[0] == "empty":
        if len(num_list) == 0:
            ans_list.append(1)
        else:
            ans_list.append(0)
    elif list[0] == "pop":
        if len(num_list) == 0:
            ans_list.append(-1)
        else:
            ans_list.append(num_list.pop())


for i in range(len(ans_list)):
    print(ans_list[i])
    