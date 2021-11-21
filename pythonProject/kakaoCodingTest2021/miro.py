rangeX = [0, 1, 0, -1]
rangeY = [-1, 0, 1, 0]

import sys
from collections import deque

grid = [list(sys.stdin.readline().strip()) for _ in range(2)]

print(grid)

def reachTheEnd(grid, maxtime):

    r = len(grid)
    c = len(grid[0])
    # if r-1 == 0 and c-1 == 0:
    #     return "YES"

    print(r, c)
    visited = [[False] * r] * c
    time_chk = [[-1] * r] * c
    q = deque()
    time_chk[0][0] = maxtime

    q.append([0, 0, maxtime])

    while q:
        now_x, now_y, this_time = q.popleft()
        for i in range(4):
            temp_x = now_x + rangeX[i]
            temp_y = now_y + rangeY[i]
            if 0 <= temp_x < r and 0 <= temp_y < c and this_time > 0:
                if grid[temp_x][temp_y] == '.' and visited[temp_x][temp_y] == False:
                    q.append([temp_x, temp_y, this_time - 1])
                    time_chk[temp_x][temp_y] = this_time - 1
                    visited[temp_x][temp_y] = True
    if time_chk[r-1][c-1] >= 0:
        return 'YES'
    else:
        return "NO"


print(reachTheEnd(grid, 9))
