N = int(input())
A = [list(map(int,input().split()))for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = A[0][0]
for i in range(N):
    for j in range(N):
        if i-1 >= 0:
            dp[i][j] = max(dp[i][j],dp[i-1][j]+A[i][j])
        if j-1 >= 0:
            dp[i][j] = max(dp[i][j],dp[i][j-1]+A[i][j])
print(dp[N-1][N-1])
