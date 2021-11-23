import sys

n, score, p = map(int, sys.stdin.readline().split())

pre_score = list(map(int, sys.stdin.readline().split()))

if n == 0:
    print(1)
else:
    if n == p and pre_score[-1] >= score:
        print(-1)
    else:
        res = n+1

        for i in range(n):
            if pre_score[i] <= score:
                res = i+1
                break
        print(res)