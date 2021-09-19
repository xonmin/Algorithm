# 백준 14502번 및 이코테
import sys
import copy
from collections import deque
from itertools import combinations

#
# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
N, M = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
copy_map = map
# logic



rangeX = [0, 1, 0, -1]
rangeY = [-1, 0, 1, 0]
ans = 0
zero_zone = []
virus_zone = []

for i in range(N):
    for j in range(M):
        if map[i][j] == 0:
            zero_zone.append([i, j])
        if map[i][j] == 2:
            virus_zone.append([i, j])
# 벽 3개 고르기
candidate_wall_list = combinations(zero_zone, 3)


def virus(x, y):
    q = deque()
    q.append([x, y])
    visit = [[False] * M for _ in range(N)]
    visit[x][y] = True
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            temp_x = now_x + rangeX[i]
            temp_y = now_y + rangeY[i]
            if 0 <= temp_x < N and 0 <= temp_y < M and visit[temp_x][temp_y] is False:
                if copy_map[temp_x][temp_y] == 0:
                    copy_map[temp_x][temp_y] = 2
                    visit[temp_x][temp_y] = True
                    q.append([temp_x, temp_y])


for wall_list in candidate_wall_list:
    copy_map = copy.deepcopy(map)

    #벽세워
    for i in range(3):
        copy_map[wall_list[i][0]][wall_list[i][1]] = 1
    #바이러스 뿌려 -> 맵 바꿔
    for spread in virus_zone:
        virus(spread[0], spread[1])
    count_zero = sum(i.count(0) for i in copy_map)
    #print("조회" ,count_zero)
    ans = max(count_zero, ans)

print(ans)
