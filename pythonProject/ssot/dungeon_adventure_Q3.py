def solution(k, dungeons):
    dp = []

    dungeons.sort(key=lambda x: x[0])

    for i in range(len(dungeons)):
        if k - (dungeons[i][0] + dungeons[i][1]) >= 0:
            dp[i + 1] = max()

    return -1