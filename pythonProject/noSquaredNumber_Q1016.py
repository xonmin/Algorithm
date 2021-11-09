# 1016번 제곱 ㄴㄴ 수

import sys
import math

mini, maxi = map(int, sys.stdin.readline().split())


# #시초
# cnt = 0
# for i in range(min, max+1):
#     for j in range(2,i+2):
#         if pow(j,2) > i:
#             cnt +=1
#             break
#         if i%pow(j,2) == 0:
#             break
#
# print(cnt)


# 2,3,5,6,7,8,10

def check_prime_num(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# max_num = int(math.sqrt(maxi))
# min_num = int(math.sqrt(mini))
#
# print(min_num, max_num)

# 1,4,9,16,25 ...

number = mini
ans = 0

# dp = list()
# dp.append(0)
# for i in range(1, 2 * maxi):
#     dp.append(i ** 2)
#
# i = 1
# print(15 % 2)

dp = [False] * (maxi - mini + 1)
i = 2

while i ** 2 <= maxi:
    num = mini // i ** 2
    while num * (i ** 2) <= maxi:
        if 0 <= num * (i ** 2) - mini <= maxi - mini:
            dp[num * (i ** 2) - mini] = True
        num += 1
    i += 1

print(dp.count(False))
