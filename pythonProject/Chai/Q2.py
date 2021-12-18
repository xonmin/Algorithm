from collections import deque


def findBeforeMatrix(after):
    N = 0
    for i in after:
        N += 1
    M = len(after[0])
    before = [[0] * M for i in range(N)]

    before[0][0] = after[0][0]

    dp = [[0] * M for i in range(N)]

    dp[0][0] = after[0][0]
    for i in range(N):
        for j in range(M):
            if i == 0 and j == 0:
                continue
            if j == 0:
                dp[i][j] = after[i][j] - after[i - 1][j]
            elif i == 0:
                dp[i][j] = after[i][j] - after[i][j - 1]
            else:
                dp[i][j] = after[i][j] - after[i - 1][j] - after[i][j - 1] + after[i - 1][j - 1]

    return dp

    # ans = ""
    # for i in range(N):
    #     tmp = "".join(str(_) for _ in before[i])
    #     #  print(tmp)
    #     ans += tmp + '\n'
    #
    # return ans


print(findBeforeMatrix([[1, 3,6,10],[2,6,12,20],[3,9,18,30],[4,12,24,40]]))
