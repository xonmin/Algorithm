# 백준 18405번 경쟁적 전염
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

cylinder = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

s, x, y = map(int, sys.stdin.readline().split())

rangeX = [0, 1, 0, -1]
rangeY = [-1, 0, 1, 0]

visited = [[False] * n for _ in range(n)]


# logic

def bfs(virus_type,x,y):
    for i in range(4):
        temp_x = x + rangeX[i]
        temp_y = y + rangeY[i]
        if 0 <= temp_x < n and 0 <= temp_y < n and visited[temp_x][temp_y] is False:
            if cylinder[temp_x][temp_y] == 0:
                cylinder[temp_x][temp_y] = virus_type
                visited[temp_x][temp_y] = True


count = 0
while count != s:
    for virus_num in range(1,k+1):
        for i in range(n):
            for j in range(n):
                if cylinder[i][j] == virus_num and visited[i][j] is False:
                    virus_type = cylinder[i][j]
                    visited[i][j] = True
                    bfs(virus_type,i,j)

    count += 1

print(cylinder[x-1][y-1])
