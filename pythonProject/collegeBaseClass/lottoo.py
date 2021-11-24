import sys
from itertools import combinations

while True:
    put = sys.stdin.readline()

    if put == '0\n':
        break

    tmp = list(map(int, put.split()))
    k = tmp.pop(0)
    S = tmp

    ans_list = list(combinations(S, 6))

    for ans in ans_list:
        print(' '.join(str(_) for _ in ans))

    print()
