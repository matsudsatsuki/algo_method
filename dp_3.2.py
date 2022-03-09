N,M = map(int,input().split())
W = list(map(int,input().split()))
dp = [[False]*(M+1)for _ in range(N+1)]
dp[0][0] = True
for i in range(N):
    for j in range(M+1):
        if not dp[i][j]:
            continue
        dp[i+1][j] = True
        if j + W[i] <= M:
            dp[i+1][j+W[i]] = True
print('Yes'if dp[N][M] else 'No')