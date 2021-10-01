# 백준 유기농 양배추 1012번

import sys
from collections import deque

earthworm_ans = []
farm = list()
visited = list()

rangeX = [0, 1, 0, -1]
rangeY = [-1, 0, 1, 0]


def bfs(x, y):
    # print("bfs 도착 ")
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    while q:
        now_x, now_y = q.popleft();
        for i in range(4):
            temp_y = now_y + rangeY[i]
            temp_x = now_x + rangeX[i]
            if 0 <= temp_x < m and 0 <= temp_y < n:
                #print("첫번째 조건 :", visited[temp_x][temp_y], "두번째 조건 : ", farm[temp_x][temp_y])
                if visited[temp_x][temp_y] is False and farm[temp_x][temp_y] == 1:
                    #print("양배추 / 접근 통과 ")
                    q.append([temp_x, temp_y])
                    visited[temp_x][temp_y] = True


t = int(sys.stdin.readline())

for u in range(0,t):
    m, n, k = map(int, sys.stdin.readline().split())
    farm = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    worm = 0
    cabbage_loc = []

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        farm[x][y] = 1


    for i in range(m):
        for j in range(n):
            if farm[i][j] == 1 and visited[i][j] is False:
                bfs(i, j)
                worm += 1

    earthworm_ans.append(worm)
    #print("한 사이클 끝 ")
for worm in earthworm_ans:
    print(worm)
