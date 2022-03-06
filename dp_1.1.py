N,X,Y = map(int,input().split())

nums = [0]*N
nums[0],nums[1] = X,Y
for i in range(2,N):
    nums[i] = (nums[i-2]+nums[i-1])%100

print(nums[N-1])