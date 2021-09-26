# 18310번 안테나 // 슈발 시간초과
import sys

n = int(sys.stdin.readline())

home_point = list(map(int,sys.stdin.readline().split()))
compare = 9999999

ans = 0
def chk_distance(base):
    sum = 0
    for home in home_point:
        sum += abs(base-home)

    return sum

home_point.sort()

for h in home_point:
    temp = chk_distance(h)
    #print('집위치  : ', h , ', 거리 :', temp)
    #print('최소가 되는 집  : ', ans)
    if compare > temp:
        compare = temp
        ans = h


print(ans)