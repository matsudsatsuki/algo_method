N,A,B = map(int,input().split())
X = list(map(int,input().split()))
dp = [[False]*A for _ in range(N+1)]
dp[0][0] = True
for i in range(N):
    for j in range(A):
        if not dp[i][j]:
            continue
        dp[i+1][j] = True
        dp[i+1][(j+X[i])%A] = True
print('Yes'if dp[N][B] else 'No')