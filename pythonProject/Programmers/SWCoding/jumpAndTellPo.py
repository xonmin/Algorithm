
def solution(n):


    dp = [999] * ( n +1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+ 1):
        if i % 2 == 0:
            dp[i] = min(dp[i // 2], dp[i - 1] + 1)
        else:
            dp[i] = dp[i - 1] + 1

    return dp[n]


print(solution(5000))

def solution1(n):
    ans = 0
    while n > 0:
        q, r = divmod(n,2)
        n = q
        if r != 0:
            ans += 1
    return ans
