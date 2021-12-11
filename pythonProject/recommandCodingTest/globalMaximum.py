from itertools import combinations


def solution(arr, m):
    INF = 100000000;

    comb = combinations(arr, m)
    globalMaximum = 0
    for com in comb:
        diff_case = combinations(com, 2)
        currentMininmum = INF

        for diff in diff_case:
            currentMininmum = min(currentMininmum, abs(diff[0] - diff[1]))

        globalMaximum = max(globalMaximum, currentMininmum)

    return globalMaximum


print(solution([1, 2, 4, 5, 8], 3))
