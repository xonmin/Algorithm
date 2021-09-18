from collections import deque
import sys
#2589번 보물섬
y, x = map(int,sys.stdin.readline().split())

map = [list(map(str,sys.stdin.readline().rstrip())) for _ in range(y)]
#로직




rangeX = [0,1,0,-1]
rangeY = [-1,0,1,0]

ans = 0

q = deque()

def bfs(row,col):
    q.append([row,col])
    c = [[0]*x for _ in range(y)]
    c[row][col] = 1
    count = 0
    while q:
        row, col = q.popleft()
        for i in range(4):
            temp_y = row + rangeY[i]
            temp_x = col + rangeX[i]
            if 0 <= temp_y < y and 0 <= temp_x < x:
                if map[temp_y][temp_x] == 'L' and c[temp_y][temp_x] == 0 :
                    c[temp_y][temp_x] = c[row][col] + 1
                    count = max(count, c[row][col])
                    q.append([temp_y, temp_x])
    return count


for i in range(y):
    for j in range(x):
        if map[i][j] == 'L':
            ans = max(ans,bfs(i,j))

print(ans)