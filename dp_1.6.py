N,M = map(int,input().split())
D = [int(x)for x in input().split()]
dp = [False]*(N+1)
dp[0] = True
for i in range(1,N+1):
    for j in range(M):
        if i - D[j] >= 0 and dp[i-D[j]]:
            dp[i] = True
if dp[N]:
    print('Yes')
else:
    print('No')

            
