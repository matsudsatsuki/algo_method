A = [[0]*4 for _ in range(4)]
A[0] = list(map(int,input().split()))
for i in range(1,4):
    for j in range(4):
        A[i][j] += A[i-1][j]
        if j-1 >= 0:
            A[i][j] += A[i-1][j-1]
        if j+1 < 4:
            A[i][j] += A[i-1][j+1]
print(A[3][3])
