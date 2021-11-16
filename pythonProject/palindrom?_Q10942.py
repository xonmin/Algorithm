# 팰린드롬? 10942번

import sys

N = int(sys.stdin.readline())

problem = sys.stdin.readline().split()
problem.insert(0,0)

M = int(sys.stdin.readline())

condi = list()

ans = list()
for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    condi.append([S, E])

dp = list()
for _ in range(N+1):
    dp.append([0]*(N+1))


def check_palindrome(n):
    if len(n) == 1:
        return 1
    half = len(n) / 2
    if len(n) % 2 == 0:
        if n[0:int(half)] == ''.join(reversed(n[int(half):])):
            return 1
    else:
        if n[0:int(half + 1)] == ''.join(reversed(n[int(half):])):
            return 1

    return 0


def dp_palindrome(problem , N):
    for i in range(1,N+1): # 한글자 회문
        dp[i][i] = 1

    for i in range(1,N): #두글자도 같으면 회문
        dp[i][i+1] = dp[i+1][i] = 1

    for i in range(2, N):  # 길이 2부터 i = s~e까지의 길이
        for j in range(1, N-i+1): # 왼쪽 끝과 오른쪽 끝이 같고, 그 사이의 수가 팰린이면 결국 팰린
            if problem[j] == problem[j + i] and dp[j + 1][j + i - 1]:
                dp[j][j + i] = dp[j + 1][j] = 1


# # 시간초과
# # for S, E in condi:
# #     new_condi = ''.join(problem[S - 1:E])
# #     ans.append(check_palindrome(new_condi))

# for _ in ans:
#     print(_)

dp_palindrome(problem,N)


for S, E in condi:
    print(dp[S][E])