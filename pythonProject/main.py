import sys
from collections import deque

# 1697번 숨바꼭질


N, K = map(int, sys.stdin.readline().split())

rng = [-1, 1, N]

chk =  [0 * _ for _ in range(100001)]

def findBrother(N, K):

    if N == K:
        return 0

    q = deque()
    q.append([N, 0])
    while q:
        now_pos,count = q.popleft()
        temp_position = [now_pos+1,now_pos-1,2*now_pos]
        for temp_pos in temp_position:
            if 0 <= temp_pos < len(chk) and chk[temp_pos] == 0:
                temp_count = count + 1
                chk[temp_pos] = temp_count
                if temp_pos == K:
                    return temp_count
                else:
                    q.append([temp_pos, temp_count])


case1 = findBrother(N,K)

print(case1)

