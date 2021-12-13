from collections import deque


def solution(p):
    p = list(p)

    def split(p):
        left = 0
        right = 0
        cut_idx = 0
        for i in range(len(p)):
            if p[i] == '(':
                left += 1
            elif p[i] == ')':
                right += 1
            if left == right:
                cut_idx = i
                break
        u, v = p[0:i + 1], p[i + 1:]

        return u, v

    def chk_correct(u):
        q = deque(u)
        left = 0
        right = 0
        chk = True
        while left >= right and q:
            bracket = q.popleft()
            if bracket == '(':
                left += 1
            elif bracket == ')':
                right += 1
        if right > left:
            chk = False
            return chk
        return chk

    def convert(string):
        string.pop(0)
        string.pop(-1)
        if not string:
            return []
        else:
            for i in range(len(string)):
                if string[i] == '(':
                    string[i] = ')'
                else:
                    string[i] = '('
            return string

    def exe(p):
        if len(p) == 0:
            return []

        u, v = split(p)

        if chk_correct(u):
            return u + exe(v)
        else:
            new_u_str = convert(u)
            return ['('] + exe(v) + [')'] + new_u_str

    return ''.join(exe(p))
