
import string


def change(n, k):
    tmp = string.digits + string.ascii_lowercase
    q, r = divmod(n, k)
    if q == 0:
        return tmp[r]
    else:
        return change(q, k) + tmp[r]



def solution(n):
    answer = ''
    temp = change(n,3)
    print(temp)
    return answer

solution(3)