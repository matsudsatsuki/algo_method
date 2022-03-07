N = int(input())
A = [[0]*N for _ in range(N)]
A[0] = list(map(int,input().split()))
for i in range(1,N):
    for j in range(N):
        A[i][j] += A[i-1][j]
        if j-1 >= 0:
            A[i][j] += A[i-1][j-1]
        if j+1 < N:
            A[i][j] += A[i-1][j+1]
        A[i][j]%=100
print(A[N-1][N-1])