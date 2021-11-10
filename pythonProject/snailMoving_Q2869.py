# 2869번 달팽이는 올라가고 싶다.

import sys
import math
a, b, v = map(int, sys.stdin.readline().split())

location = 0
day = 1

v //(a-b) + a

print( math.ceil((v-a)/ (a-b)) + 1)