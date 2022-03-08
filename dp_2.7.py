N = int(input())
A = [list(map(int,input().split()))for _ in range(N)]
inf = 1e9
dp = [[inf]*N for _ in range(N)]
dp[0][N-1] = A[0][N-1]
for i in range(N):
    for j in range(N-1,-1,-1):
        if i-1 >= 0:
            dp[i][j] = min(dp[i][j],dp[i-1][j]+A[i][j])
        if j+1 < N:
            dp[i][j] = min(dp[i][j],dp[i][j+1]+A[i][j])
print(dp[N-1][0])