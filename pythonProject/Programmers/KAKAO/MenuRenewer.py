from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for c in course:
        tmp = []
        for order in orders:
            cmb = combinations(sorted(order), c)
            tmp += cmb

        counter = Counter(tmp)
        # 겹치는 메뉴가 없던지, 혹은 혼자 주문한 것이 아니라면,
        if len(counter) != 0  and max(counter.values()) != 1:
            answer += [''.join(remenu) for remenu in counter if counter[remenu] == max(counter.values())]

    answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
