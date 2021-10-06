# 백준 18405번 경쟁적 전염
import copy
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

cylinder = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#본 레포 테스트
s, x, y = map(int, sys.stdin.readline().split())

rangeX = [0, 1, 0, -1]
rangeY = [-1, 0, 1, 0]

visited = [[False] * n for _ in range(n)]

virus = []


# logic

def bfs(virus_type, x, y):
    visited[x][y] = True
    for i in range(4):
        temp_x = x + rangeX[i]
        temp_y = y + rangeY[i]
        if 0 <= temp_x < n and 0 <= temp_y < n and visited[temp_x][temp_y] is False:
            if cylinder[temp_x][temp_y] == 0:
                cylinder[temp_x][temp_y] = virus_type
                visited[temp_x][temp_y] = True

while s:
    new_cylinder = copy.deepcopy(cylinder)
    for i in range(n):
        for j in range(n):
            if cylinder[i][j] != 0:
                virus.append((cylinder[i][j], i, j))
    virus.sort()
    for virus_type, i, j in virus:
        bfs(virus_type,i,j)
    if cylinder[x-1][y-1]:
        break
    s -= 1



print(cylinder[x - 1][y - 1])
