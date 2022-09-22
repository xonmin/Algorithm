import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n + 1)]
dp[1] = seq[0]

for i in range(2, n + 1):
    if seq[i] > max(seq[:i]):
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]


print(dp[-1])