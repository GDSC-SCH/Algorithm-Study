#사용자로부터 입력을 받는다
a, b = (map(int, input().split(' ')))

arr = []

#a만큼 반복을 수행하며 배열에 수를 추가
for i in range(a):
    arr.append(int(input()))

#동전 크기가 역순이 되도록 정렬 수행
arr.sort(reverse = True)

#카운트 변수 선언
cnt = 0

# 배열의 길이만큼 반복을 수행
for j in range(len(arr)):

    #b를 배열의 가장 큰 동전부터 나눈 몫을 카운트 변수에 추가
    cnt += int(b/arr[j])
    #b는 배열의 요소의 가장 큰 동전으로 나눈 나머지로 재할당
    b = b%arr[j]

#카운트 변수 출력
print(cnt)
    

