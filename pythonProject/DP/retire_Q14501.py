#백준 14501 - 퇴사 / 이코테 177p
import copy
import sys


n = int(sys.stdin.readline())

consult = list()
consult.append([0,0])

for _ in range(n):
    t, p = map(int, sys.stdin.readline().split())
    consult.append([t,p])


dp = [0 for i in range(n+1)]

for i in range(n-1,-1,-1):  #뒤에서 부터 DP
    # N 번째 날은 N+1 기준 수익과 N번째 날 수익 + Tn 중 큰 값 고르기
    if i + consult[i][0] > n:
        dp[i] = dp[i+1]
    else :
        dp[i] = max(consult[i][1] + dp[i + consult[i][0]],dp[i+1])
print(dp[0])