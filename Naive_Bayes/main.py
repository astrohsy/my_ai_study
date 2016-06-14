# TSP
n = int(input())
D = [[1000000000 for i in range(20)] for j in range(1 << n)]
P = [[[] for i in range(20)] for j in range(1 << n)]
G = []

for i in range(n):
    G.append(list(map(int, input().split())))

D[1][0] = 0;
P[1][0] = [1]
for s in range(1 << n):
    for i in range(n):
        if not s & (1 << i):
            continue
        for j in range(n):
            if s & (1 << j):
                continue
            if G[i][j] != 0:
                if D[s | 1 << j][j] > D[s][i] + G[i][j]:
                    D[s | 1 << j][j] = D[s][i] + G[i][j]
                    P[s | 1 << j][j] = P[s][i].copy()
                    P[s | 1 << j][j].append(j + 1)

ans, index = 1000000000, 0
for i in range(n):
    if ans > D[(1 << n) - 1][i] + G[i][0]:
        ans = D[(1 << n) - 1][i] + G[i][0]
        index = i

# 최적해 출력
print(ans)

# 경로 출력
for i in P[(1 << n) - 1][index]:
    print(i)
