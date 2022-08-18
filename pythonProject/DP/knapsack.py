import sys

n, k = map(int, sys.stdin.readline().split())
item = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

# 행 : 남은 무게
bag = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    w, v = item[i - 1]
    for j in range(1, k + 1):
        if w > j:  # 못 넣을 때,
            bag[i][j] = bag[i - 1][j]
        else:  # 가치 확인
            bag[i][j] = max(bag[i - 1][j], bag[i - 1][j - w] + v)

print(bag[n][k])