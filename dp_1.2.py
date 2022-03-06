N = int(input())
dp = [0]*N
steps = [int(x)for x in input().split()]
dp[1] = steps[1]
for i in range(2,N):
    dp[i] = min(dp[i-1]+steps[i],dp[i-2]+steps[i]*2)
print(dp[-1])