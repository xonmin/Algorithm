import sys
from collections import deque

def solution(miro,n,m):
    ans = 0
    q = deque()
    rangeX = [0, 1, 0, -1]
    rangeY = [-1, 0, 1, 0]
    q.append([0,0,1])
    visited = [[False]*m for i in range(n)]
    visited[0][0] = True

    while q:
        x, y, cnt = q.popleft()

        if x == n-1 and y == m- 1:
            return cnt
        for i in range(4):
            nx = x + rangeX[i]
            ny = y + rangeY[i]

            if 0<= nx < n and 0<= ny <m and visited[nx][ny] is False:
                if miro[nx][ny] == 1:
                    q.append([nx,ny,cnt+1])
                    visited[nx][ny] = True
    return ans


n, m = map(int, sys.stdin.readline().split())

miro = [list(map(int,sys.stdin.readline().strip())) for i in range(n)]


print(solution(miro,n,m))