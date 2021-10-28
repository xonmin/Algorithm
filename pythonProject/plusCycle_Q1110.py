#더하기 사이클 Q1110

import sys


N = int(sys.stdin.readline())



contrast = 0
ans = 0

new_int = N
if N == 0 :
    print(1)
    exit(0)

while N != contrast:
    if new_int < 10:
        first = 0
        second = new_int
    else:
        first = new_int // 10
        #print(first)
        second = new_int % 10
        #print(second)

    new_int = second*10 + (first+second)%10
    contrast = new_int
    #print(contrast)
    ans += 1


print(ans)
