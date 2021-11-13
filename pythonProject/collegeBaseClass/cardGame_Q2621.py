# 대학생기본반 2621 카드게임


import sys

deck = list()

color = [0]*4  # R G B Y
num = [0] * 10

max_int = 0
for _ in range(5):
    now_color, number = sys.stdin.readline().split()
    if now_color == 'R':
        color[0] += 1
    elif now_color == 'G':
        color[1] += 1
    elif now_color == 'B':
        color[2] += 1
    else:
        color[3] += 1

    number = int(number)
    num[number] += 1
    max_int = max(max_int,number)
    deck.append([now_color, number])

ans = 100 + max_int

# case 1
if max(color) == 5:
    start = num.index(1)
    for _ in range(1, 5):
        if start + _ >= 10:
            break
        if num[start + _] == 1:
            if _ == 4:
                ans = max(900 + max_int, ans)
            continue
        else:
            # 플러쉬
            ans = max(600 + max_int, ans)
            break
# 포카드
if 4 in num:
    ans = max(num.index(4) + 800, ans)

if max(num) == 3:
    if 2 in num:
        # 풀하우스
        ans = max(num.index(3) * 10 + num.index(2) + 700, ans)
    else:
        # 트리플
        ans = max(400 + num.index(3), ans)

if 1 in num:
    #스트레이트
    start = num.index(1)
    for i in range(1, 5):
        if start + i >= 10:
            break
        if num[start + i] == 1:
            if i == 4:
                ans = max(500 + max_int, ans)
        else:
            break

#더블
if max(num) == 2:
    if num.count(2) == 2: # 따따블
        ans = max(300 + num.index(2,num.index(2)+1) *10+ num.index(2),ans)
    else :
        ans = max(num.index(2) +200,ans)

print(ans)