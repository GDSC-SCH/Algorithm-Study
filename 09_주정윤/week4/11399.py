# 사람의 수
N = int(input())

time = list(map(int, input().split()))

time.sort()
sum=0
sum2=0
sum_list=[]

for i in range(N):
    sum = sum + time[i] 
    sum2 = sum2+sum
 

print(sum2)
