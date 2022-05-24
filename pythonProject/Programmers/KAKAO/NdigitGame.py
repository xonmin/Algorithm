import string


def change(n, k):
    tmp = string.digits + string.ascii_lowercase
    q, r = divmod(n, k)
    if q == 0:
        return tmp[r]
    else:
        return change(q, k) + tmp[r]

print(change(18,2))

def solution(n, t, m, p):
    # 진법 , 숫자 개수, 게임 인원, 튜브 순서
    answer = ''

    number = 0
    while len(answer) != t:
        this_num = change(number, n)

        for i in range(len(this_num)):

    return answer
