import sys


def solution(S, T):
    # S -> T
    '''
    문자열의 뒤에 A를 추가
    문자열의 뒤에 B를 추가하고 문자열 뒤집기
    '''

    def chkA(test_str):
        return test_str + 'A'

    def chkB(test_str):
        add_B = test_str + 'B'
        reverse_B = "".join(reversed(add_B))
        return reverse_B

    def exec(S):
        if len(S) <= len(T):
            if len(S) == len(T):
                if S == T:
                    print(1)
                    return
                else:
                    print(0)
                    return

            new_S1 = chkA(S)
            new_S2 = chkB(S)
            exec(new_S1)
            exec(new_S2)

    exec(S)


S = sys.stdin.readline()
T = sys.stdin.readline()

print(solution(S, T))
