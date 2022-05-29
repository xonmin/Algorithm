import sys

stair = []
n = int(sys.stdin.readline())
for i in range(n):
    stair.append(int(sys.stdin.readline()))

dp = [0 for i in range(n)]

if n == 1:
    print(stair[0])
    exit(0)
if n == 2:
    print(sum(stair))
    exit(0)

dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
for i in range(3, n):
    dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])

print(dp[-1])
