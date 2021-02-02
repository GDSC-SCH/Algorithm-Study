
N = int(input())

w_list=[]
h_list=[]
count_list=[]

# 각각의 리스트에 값 삽입
for i in range(N):
    weight, height = map(int, input().split())
    w_list.append(weight)
    h_list.append(height)

# 리스트 뒤져서 키와 몸무게가 모두 자신보다 큰 사람 수 찾기
for i in range(N):
    count=0
    for j in range(N):
        if w_list[i]<w_list[j] and h_list[i]<h_list[j]:
            count+=1
    count_list.append(count+1)

# 출력
for i in range(N):
    print(count_list[i], end=' ')


