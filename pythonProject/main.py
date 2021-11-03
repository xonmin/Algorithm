import sys
from collections import deque
import copy

# 백준 1987번 알파벳

r, c = map(int, sys.stdin.readline().split())

board = [list(map(lambda x : ord(x)-65,sys.stdin.readline().rstrip())) for _ in range(r)]
#테스트
rangeX = [0, 1, 0, -1]
rangeY = [-1, 0, 1, 0]
ch = [0] * 26

def dfs(fp, x, y):
    global ans
    ans = max(ans,fp)

    for i in range(4):
        temp_x = x + rangeX[i]
        temp_y = y + rangeY[i]

        if 0 <= temp_x < r and 0 <= temp_y < c and ch[board[temp_x][temp_y]] == 0 :
            ch[board[temp_x][temp_y]] = 1
            dfs(fp+1, temp_x, temp_y)
            ch[board[temp_x][temp_y]] = 0


ch[board[0][0]] = 1
ans = 1
dfs(ans, 0, 0)

# print(visited)
print(ans)