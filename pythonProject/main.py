import sys
from collections import deque

# 1697번 숨바꼭질


N, K = map(int, sys.stdin.readline().split())

rng = [-1, 1, N]


def findBrother(N, K):

    if N == K:
        return 1

    q = deque()
    q.append([N, 1])
    while q:
        now_pos,count = q.popleft()
        temp_position = [now_pos+1,now_pos-1,2*now_pos]
        for temp_pos in temp_position:
            if 0 <= temp_pos <= 100000:
                temp_count = count + 1
                if temp_pos == K:
                    return temp_count
                else:
                    q.append([temp_pos, temp_count])


case1 = findBrother(N+1,K)
#print(case1)
case2 = findBrother(N-1,K)
#print(case2)
case3 = findBrother(2*N,K)
#print(case3)
ans = min(case1,min(case2,case3))

print(ans)