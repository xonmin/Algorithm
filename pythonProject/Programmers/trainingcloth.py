import copy


def solution(n, lost, reserve):
    reserve_l = list(set(reserve) - set(lost))
    lost_l = list(set(lost) - set(reserve))
    lost = sorted(lost_l)
    reserve = sorted(reserve_l)
    last = copy.deepcopy(lost)
    for st in last:
        if st - 1 in reserve:
            reserve.remove(st - 1)
            lost.remove(st)
        elif st + 1 in reserve:
            reserve.remove(st + 1)
            lost.remove(st)

    return n - len(lost)


print(solution(5, [2, 3], [3, 4]))
print(solution(5, [4, 2], [3, 5]))
print(solution(3,[1],[1]))