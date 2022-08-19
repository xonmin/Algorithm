def solution(k, dungeons):
    l = len(dungeons)
    hp = [[[k, 0] for _ in range(k + 1)] for _ in range(l + 1)]
    remain_hp = k
    explore = 0
    for i in range(1, l + 1):
        required, use = dungeons[i - 1]
        for j in range(1, k + 1):
            if remain_hp < required:
                hp[i][j] = hp[i - 1][j]
            else:
                if hp[i - 1][j][0] < hp[i - 1][j - required][0] - use:
                    hp[i][j] = hp[i - 1][j]
                else:
                    hp[i][j][0] = hp[i - 1][j - required][0] - use
                    hp[i][j][1] = hp[i - 1][j - required][1] + 1
                    explore = max(explore, hp[i][j][1])
    return explore


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
