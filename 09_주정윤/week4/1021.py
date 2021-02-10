N, M = map(int, input().split())
index = list(map(int, input().split()))

count=0
list = [i for i in range(1, N+1)]

for i in range(M):
    # 타켓 인덱스 값 가져오기
    target_index = list.index(index[i])

    # 찾는 값의 원소가 앞쪽에 있을 때
    if target_index < len(list) - target_index:
        while True:
            # 뽑아내기
            if list[0]==index[i]:
                del list[0]
                break
            else:
                list.append(list[0])
                del list[0]
                count+=1
    else: # 찾는 값의 원소가 뒤에 있을 때
        while True:
            if list[0]==index[i]:
                del list[0]
                break
            else:
                list.insert(0, list[-1])
                del list[-1]
                count+=1

print(count)



