N = int(input())
W = list(map(int,input().split()))
M = sum(W)
dp = [[False]*(M+1)for _ in range(N+1)]
dp[0][0] = True
for i in range(N):
    for j in range(M+1):
        if not dp[i][j]:
            continue
        dp[i+1][j+W[i]] = True
        dp[i+1][abs(j-W[i])] = True
res = 0
while not dp[N][res]:
    res += 1
print(res)