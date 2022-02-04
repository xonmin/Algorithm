import sys

n, m, x, y, k = map(int, sys.stdin.readline().split())

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

field = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

moving = list(map(int, sys.stdin.readline().split()))

dice_side = [0, 0, 0, 0, 0, 0]


def check(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False


for act in moving:
    direction = act - 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    if not check(nx, ny):
        continue
    # 주사위 돌리기
    if direction == 0:  # 동쪽
        dice_side[0], dice_side[2], dice_side[3], dice_side[5] = dice_side[3], dice_side[0], dice_side[5], dice_side[2]
    elif direction == 1:  # 서
        dice_side[0], dice_side[2], dice_side[3], dice_side[5] = dice_side[2], dice_side[5], dice_side[0], dice_side[3]
    elif direction == 2:  # 북
        dice_side[0], dice_side[1], dice_side[4], dice_side[5] = dice_side[4], dice_side[0], dice_side[5], dice_side[1]
    else:
        dice_side[0], dice_side[1], dice_side[4], dice_side[5] = dice_side[1], dice_side[5], dice_side[0], dice_side[4]

    if field[nx][ny] == 0:
        field[nx][ny] = dice_side[5]
    else:
        dice_side[5] = field[nx][ny]
        field[nx][ny] = 0
    x, y = nx, ny
    print(dice_side[0])
