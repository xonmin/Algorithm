import sys

n, m = map(int, sys.stdin.readline().split())

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

x, y, dir = map(int, sys.stdin.readline().split())

room = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

answer = 0


def clean(x, y):
    global answer
    visited[x][y] = True
    answer += 1


def check_valid_location(x, y):
    if 0 <= x < n and 0 <= y < m:
        if room[x][y] == 0:
            return True
    else:
        return False


def check_unclean_left(x, y):
    if visited[x][y]:
        return False
    else:
        return True


def behid_is_wall(x, y, dir):
    back_dir = divmod(dir + 2, 4)[1]

    if room[x + dx[back_dir]][y + dy[back_dir]] == 1:
        return True
    else:
        return False


def search_clean_place(x, y, dir):
    for i in range(4):
        dir = divmod(dir + 3, 4)[1]
        temp_x, temp_y = x + dx[dir], y + dy[dir]
        if check_valid_location(temp_x, temp_y):  # 갈 수 있어
            if check_unclean_left(temp_x, temp_y):  # 왼쪽에 청소 안했어
                return True
    return False


clean(x, y)

while True:
    while search_clean_place(x, y, dir):
        for i in range(4):
            # 왼쪽 방향으로 돌아
            dir = divmod(dir + 3, 4)[1]
            temp_x, temp_y = x + dx[dir], y + dy[dir]
            if check_valid_location(temp_x, temp_y):  # 갈 수 있어
                if check_unclean_left(temp_x, temp_y):  # 왼쪽에 청소 안했어
                    clean(temp_x, temp_y)  # 치워
                    x, y = temp_x, temp_y
                    break
                else:
                    continue

    if behid_is_wall(x, y, dir):
        break
    x, y = x + dx[divmod(dir + 2, 4)[1]], y + dy[divmod(dir + 2, 4)[1]]

print(answer)
