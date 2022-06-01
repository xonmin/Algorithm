def solution(lottos, win_nums):
    zero_count = lottos.count(0)
    same = set(lottos) & set(win_nums)
    under_bounded, upper_bounded = len(same), len(same) + zero_count
    if upper_bounded == 6:
        best = 1
    elif upper_bounded == 5:
        best = 2
    elif upper_bounded == 4:
        best = 3
    elif upper_bounded == 3:
        best = 4
    elif upper_bounded == 2:
        best = 5
    else:
        best = 6
    if under_bounded == 6:
        worst = 1
    elif under_bounded == 5:
        worst = 2
    elif under_bounded == 4:
        worst = 3
    elif under_bounded == 3:
        worst = 4
    elif under_bounded == 2:
        worst = 5
    else:
        worst = 6

    return [best, worst]

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35]))