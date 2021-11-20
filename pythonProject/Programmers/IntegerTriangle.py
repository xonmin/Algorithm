def solution(triangle):

    len_tri = len(triangle[-1])

    dp = list()
    for i in range(1, len_tri + 1):
        dp.append([0] * i)

    dp[0] = triangle[0]

    for i in range(1, len_tri):
        for j in range(i+1):

            if j == 0:
                dp[i][j] += dp[i - 1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] += dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] += max(dp[i - 1][j - 1] + triangle[i][j], dp[i - 1][j] + triangle[i][j])

    return max(dp[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))