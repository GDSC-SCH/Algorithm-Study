# 테스트 데이터 입력
T = int(input())

# 테스트 데이터만큼 반복하여 dp 값 찾기
for _ in range(T):
    K = int(input())
    num = list(map(int, input().split()))

    # 최소비용값을 구하는 이중포문
    dp = [[0]*K for _ in range(K)]
    for i in range(K-1):
        dp[i][i+1] = num[i]+num[i+1]
        for j in range(i+2, K):
            dp[i][j] = dp[i][j-1] + num[j]
    
    # 최소값을 구해서 최소비용값에 합을 더해준다. 최종 최소비용값 = 최소비용값 + 최소값
    for d in range(2, K):
        for i in range(K-d):
            j = i+d
            mini = [dp[i][k] + dp[k+1][j] for k in range(i, j)]
            dp[i][j] += min(mini)
    
    print(dp[0][K-1])
