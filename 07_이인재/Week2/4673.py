#배열을 set형식으로 선언
numbers = set(range(1, 10000))

rm_set = set()  
for num in numbers :
    for n in str(num):
        num += int(n)
    #집합에 요소 추가
    rm_set.add(num)

# 기존의 배열에서 제거 대상인 수를 제거
selfNumbers = numbers - rm_set  
#정렬 후 출력
for self_num in sorted(selfNumbers):
    print(self_num)