import sys


def solution(S, T):
    # S -> T
    """
    문자열의 뒤에 A를 추가
    문자열의 뒤에 B를 추가하고 문자열 뒤집기
    T -> S 로 찾기

    S -> T
    CASE 1 A-A : 1번 연산
    CASE 2 A-B  : X
    CASE 3 B-A 둘다
    CASE 4 B-B 2번
    """

    def dfs(T):
        if T == S:
            return 1
        if len(T) <= len(S):
            return 0

        rtn = 0
        if T[-1] == 'A':
            rtn = dfs(T[:-1])

        if rtn == 1:
            return 1
        if T[0] == 'B':
            tmp_T = T[::-1]
            rtn = dfs(tmp_T[:-1])
        return rtn

    return dfs(T)

S = list(sys.stdin.readline().rstrip())
T = list(sys.stdin.readline().rstrip())

print(solution(S, T))
