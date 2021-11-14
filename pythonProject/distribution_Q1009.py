# 1009 분산처리

import sys

t = int(sys.stdin.readline())

data= list()

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    if b == 0:
        data.append(pow(a,0))
    if a == 5 or a == 6:
        data.append(a)
    else:
        q, r = divmod(b,4)
        if r == 0:
            r = 4
        data.append(pow(a,r) % 10)

for i in range(t):
    com = data[i]
    if com == 0:
        com = 10
    print(com)

#1 2 4 8 6 2
#1 3 9 7 1 3
#1 4 6 4 6 4
#1 6 6 6 6
#1 7 9 3 1 7
#1 8 4 2 6 8
#1 9 1