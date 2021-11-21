#11052번 카드 구매하기

import sys

'''

카드 i 개 = Pi 원
비싸면 높은 등급 카드 있을 확률 up
돈을 최대한 써서 구매하자 
구매하려는 카드 N 개
Pi  = P1 ~ Pn 까지 주어짐
'''

n = int(sys.stdin.readline())

card_pack = list(map(int,sys.stdin.readline().split()))
card_pack.insert(0,0)
dp = [0] * (n+1)
dp[1] = card_pack[1]


for i in range(2,n+1):
    dp[i] = card_pack[i]
    for j in range(1,n):
        dp[i] = max(dp[j] + dp[i-j],dp[i])

print(dp[-1])
