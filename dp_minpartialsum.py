N,M = map(int,input().split())
A = list(map(int,input().split()))
inf = 1e9
dp = [[inf]*(M+1)for _ in range(N+1)]

dp[0][0] = 0

for i in range(N):
    for j in range(M+1):
        if dp[i][j] == inf:continue
        dp[i+1][j] = min(dp[i+1][j],dp[i][j])
        if j+A[i]<=M:
            dp[i+1][j+A[i]] = min(dp[i+1][j+A[i]],dp[i][j]+1)
print(dp[N][M] if dp[N][M] != inf else -1)

