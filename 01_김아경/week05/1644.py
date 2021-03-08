N = int(input())    

# 소수
prime = [True for _ in range(N+1)]
prime[0] = False
prime[1] = False

for i in range(2, N+1):
    if prime[i]:
        for j in range(i*2, N+1, i):
            prime[j] = False
            
data = [i for i, boolean in enumerate(prime) if boolean]

# 투포인터 
output = 0
end_idx = 0

for i in range(len(data)):
    #print('start ', data[i])
    start_idx = i
    while start_idx <= end_idx:
        total_sum = sum(data[start_idx:end_idx])
        #print('total sum ', total_sum)
        if total_sum == N:
            output += 1
            break
        elif total_sum < N:
            end_idx += 1
        else:
            break
        
        # 소수 합으로 못 구하는 숫자
        if end_idx > len(data):
            break

print(output)