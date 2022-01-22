from itertools import permutations


def solution(v):
    answer = -1

    cases = list(permutations(v))

    for c in cases:
        tmp = 0
        for i in range(len(v) - 1):
            tmp += abs(c[i] - c[i + 1])

        answer = max(tmp, answer)
    return answer
