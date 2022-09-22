n = int(input())
dp = [[0] * 2 for i in range(n+2)] # 1번 조건을 만족 하는데 0으로 끝나는 애 , 1로 끝나는 애
dp[1][1], dp[2][0] = 1, 1
if n == 1 or n == 2:
    print(1)
    exit(0)
if n >= 3:
    for i in range(3, n + 1):
        pre_end_zero, pre_end_one = dp[i - 1]
        dp[i][0] = pre_end_zero + pre_end_one
        dp[i][1] = pre_end_zero

print(sum(dp[n]))
