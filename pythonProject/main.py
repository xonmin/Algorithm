import sys
from collections import deque
import copy

# 백준 1987번 알파벳

r, c = map(int, sys.stdin.readline().split())

board = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

rangeX = [0, 1, 0, -1]
rangeY = [-1, 0, 1, 0]
visited = [[0] * c for _ in range(r)]

max_count = 0

foot_print = list()


def dfs(fp, x, y):
    for i in range(4):
        temp_x = x + rangeX[i]
        temp_y = y + rangeY[i]
        new_fp = copy.deepcopy(fp)
        if 0 <= temp_x < r and 0 <= temp_y < c:
            if board[temp_x][temp_y] not in fp:
                new_fp.append(board[temp_x][temp_y])
                visited[temp_x][temp_y] = visited[x][y] + 1
                dfs(new_fp, temp_x, temp_y)


visited[0][0] = 1
foot_print.append(board[0][0])
dfs(foot_print, 0, 0)

# print(visited)
print(max(map(max, visited)))
