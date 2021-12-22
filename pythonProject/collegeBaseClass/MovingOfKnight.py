import sys
from collections import deque


def solution():

    def bfs(x, y, l, goal_x, goal_y):
        if x == goal_x and y == goal_y:
            return 0
        rangeX = [-2, -1, 1, 2, 2, 1, -1, -2]
        rangeY = [1, 2, 2, 1, -1, -2, -2, -1]
        visited = [[False] * l for _ in range(l)]

        q = deque()
        q.append([x, y, 0])
        visited[x][y] = True

        while q:
            now_x, now_y, cnt = q.popleft()
            for i in range(8):
                temp_x = now_x + rangeX[i]
                temp_y = now_y + rangeY[i]
                if 0 <= temp_x < l and 0 <= temp_y < l and visited[temp_x][temp_y] is False:
                    if temp_x == goal_x and temp_y == goal_y:
                        return cnt + 1
                    visited[temp_x][temp_y] = True
                    q.append([temp_x, temp_y, cnt + 1])

    def exe():
        t = int(sys.stdin.readline())
        ans_list = []
        for i in range(t):
            line = int(sys.stdin.readline())
            x, y = map(int, sys.stdin.readline().split())
            g_x, g_y = map(int, sys.stdin.readline().split())
            ans = bfs(x, y, line, g_x, g_y)
            ans_list.append(ans)

        for i in ans_list:
            print(i)
    exe()


solution()
