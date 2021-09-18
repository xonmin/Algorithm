# 1652번 누울 자리를 찾아라


# 입력
n = int(input())
room = [list(input().strip()) for _ in range(n)]

# 로직
# 가로 먼저 찾고
# 세로 먼저 찾고

horizon_count = 0
vertical_count = 0
chk_area = 0

for i in range(n):
    chk_area = 0
    for j in range(n):
        # X라면
        if room[i][j] == 'X':
            if (chk_area > 1):
                horizon_count += 1
            chk_area = 0
        elif j == n - 1:  # 마지막이라면
            if room[i][j] == '.':
                chk_area += 1
            if (chk_area > 1):
                horizon_count += 1
        # X도 아니고 마지막도 아니라면
        else:
            chk_area += 1

for i in range(n):
    chk_area = 0
    for j in range(n):
        # X라면
        if room[j][i] == 'X':
            if chk_area > 1:
                vertical_count += 1
            chk_area = 0
        elif j == n - 1:  # 마지막이라면
            if room[j][i] == '.':
                chk_area += 1
            if chk_area > 1:
                vertical_count += 1
        # X도 아니고 마지막도 아니라면
        else:
            chk_area += 1

print(horizon_count, vertical_count)