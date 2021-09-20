
# 카카오 코딩테스트 2번 문제
import string


def change(n, k):
    tmp = string.digits + string.ascii_lowercase
    q, r = divmod(n, k)
    if q == 0:
        return tmp[r]
    else:
        return change(q, k) + tmp[r]


def check_prime_num(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def soltion(n, k):
    change_k = change(n, k)
    candi_prime = change_k.split('0')
    while '' in candi_prime:
        candi_prime.remove('')
    candi_prime = list(map(int,candi_prime))

    ans = 0
    for prime_num in candi_prime:
        if check_prime_num(prime_num):
            ans += 1
    return ans

print(soltion(110011, 10))
