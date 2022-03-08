N = int(input())
tr = [[0]*N for _ in range(N)]
tr[0][0] = 1
for i in range(N):
    for j in range(N):
        if i-1 >= 0:
            tr[i][j] += tr[i-1][j]
        if j-1 >= 0:
            tr[i][j] += tr[i][j-1]
print(tr[N-1][N-1])