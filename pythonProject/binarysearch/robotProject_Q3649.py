import bisect
import sys
from collections import defaultdict

while True:
    try:
        x = int(sys.stdin.readline()) * 10000000
        n = int(sys.stdin.readline())

        lego = defaultdict(int)
        lego_list = []
        ans_candidate = []
        for i in range(n):
            l = int(sys.stdin.readline())
            lego[l] += 1
            lego_list.append(l)


        for l in lego_list:

            remain = x - l
            lego[l] -= 1

            if remain in lego:  # 딕셔너리에 나머지가 있으면
                if lego[remain] != 0:  # 이 떄 해당 레고 개수가 0이상이면
                    ans_candidate.append([l, remain])

        if ans_candidate:
            ans = [0, 0]
            for l in ans_candidate:
                if abs(ans[0] - ans[1]) <= abs(l[0] - l[1]):
                    if l[0] > l[1]:
                        ans = [l[1], l[0]]
                    else:
                        ans = [l[0], l[1]]
            print("yes", ans[0],ans[1])
        else:
            print("danger")

    except:
        break