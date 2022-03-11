N,M = map(int,input().split())
A,B = [],[]
for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
inf = 1e9
dp = [[inf]*(M+1)for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    for j in range(M+1):
        if dp[i][j] != inf:
            dp[i+1][j] = 0
        if j>=A[i]:
            if dp[i][j-A[i]] != inf:
                dp[i+1][j] = min(dp[i+1][j],1)
            if dp[i+1][j-A[i]] < B[i]:
                dp[i+1][j] = min(dp[i+1][j-A[i]]+1,dp[i+1][j])

print('Yes' if dp[N][M] != inf else 'No')
