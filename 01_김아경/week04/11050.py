N, K = map(int, input().split())

if N-K < K :
    K = N - K
    
numer = 1  # 분자
deno = 1   # 분모

for i in range(1, K+1):
    numer *= (N-i+1)
    deno *= i
    
print(numer//deno)