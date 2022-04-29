import sys
from itertools import combinations

n = int(sys.stdin.readline())
synergy = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
member_seq = [i for i in range(n)]
comb = combinations(member_seq, n // 2)

answer = 999999999

for case in comb:
    other = [m for m in member_seq if m not in case]
    t1, t2 = 0, 0
    for idx, i in enumerate(case):
        for j in case[idx:]:
            t1 += synergy[i][j]
            t1 += synergy[j][i]

    for idx, i in enumerate(other):
        for j in other[idx:]:
            t2 += synergy[i][j]
            t2 += synergy[j][i]
    if abs(t1 - t2) < answer:
        answer = abs(t1 - t2)

print(answer)