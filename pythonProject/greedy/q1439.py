import sys


def solution():
    # rule
    # 0,1 string
    # do : continuous int reverse
    s = sys.stdin.readline()

    # - 연속된 숫자들의 partition 개수
    # - 더 적은 파티션 개수번 만큼 뒤집기
    count = [0, 0]

    if s[0] == '1':
        count[1] += 1
    else:
        count[0] += 1

    now = s[0]

    for n in s[1:]:
        if n == now:
            continue
        else:
            now = n
            count[int(n)] += 1

    print(min(count[0], count[1]))
