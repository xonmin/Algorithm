# 18310번 안테나 // 정답
import sys

n = int(sys.stdin.readline())

home_point = list(map(int,sys.stdin.readline().split()))

home_point.sort()

print(home_point[(n-1) // 2] )