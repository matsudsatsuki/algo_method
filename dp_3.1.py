N,M = map(int,input().split())
A = list(map(int,input().split()))
dp = [[False]*M for _ in range(N)]
dp[0][0] = True
for i in range(N-1):
    for j in range(M):
        if not dp[i][j]:
            continue
        dp[i+1][j] = True
        if j+A[i] < M:
            dp[i+1][j+A[i]] = True
print(sum(dp[N-1]))
