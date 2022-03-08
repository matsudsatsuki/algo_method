N = int(input())
S = [input()for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if S[i][j] == '#':
            continue
        if i-1 >= 0:
            dp[i][j] += dp[i-1][j]
        if j-1 >= 0:
            dp[i][j] += dp[i][j-1]
print(dp[N-1][N-1])