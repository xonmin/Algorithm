# 줄세우기 q2631
# LIS (Longest Increasing Subsequence (최장 증가 부분 수열)
# but 지금 구현한 코드는 O(n^2)
# 이진 분류를 통해 lowerBound 를 통해 LIS 의 길이를 구하는 O(nlog(n)) 알고리즘 존재
import sys

n = int(sys.stdin.readline())

children = [ ]

for _ in range(n):
    children.append(int(sys.stdin.readline()))

maxi = 0
length = [0]*n
length[0] = children[0]
print(children)
for i in range(n):
    length[i] = 1;
    for j in range(i):
        if children[j] < children[i]:
            length[i] = max(length[j] + 1,length[i])
print(length)
print(n - max(length))