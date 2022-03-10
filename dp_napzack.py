N,W = map(int,input().split())
weight = []
value = []
for _ in range(N):
    a,b = map(int,input().split())
    weight.append(a)
    value.append(b)
dp = [[-1]*(W+1)for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    for j in range(W+1):
        dp[i+1][j] = max(dp[i+1][j],dp[i][j])
        if j+weight[i] <= W:
            dp[i+1][j+weight[i]] = max(dp[i+1][j+weight[i]],dp[i][j]+value[i])
print(max(dp[N]))


