#효율성 문제
def solution(n):
    dp = [1000000000 for i in range(n + 1)]
    if n == 3 or n == 5:
        return 1
    if n == 4:
        return -1
    dp[3], dp[5] = 1, 1

    for i in range(6, n + 1):
        dp[i] = min(dp[i - 5] + 1, dp[i - 3] + 1)

    if dp[n] > 1000000000:
        return -1
    print(dp)
    return dp[n]


print(solution(15555))
# if i % 15 == 0:
#     dp[i] = min(dp[i - 5] + 1, dp[i - 3] + 1)
# elif i % 5 == 0:
#     dp[i] = min(dp[i - 5] + 1, dp[i - 3] + 1)
# elif i % 3 == 0:
#     dp[i] = min(dp[i - 3] + 1, dp[i - 5] + 1)
# else:
#     dp[i] = min(dp[i - 3] + 1, dp[i - 5] + 1)
