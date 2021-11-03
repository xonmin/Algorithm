# Q1747
import sys

N = int(sys.stdin.readline())


def check_prime_num(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def check_palindrome(n):
    if len(n) == 1:
        return True
    half = len(n)/2
    if len(n) % 2 == 0:
        if n[0:int(half)] == ''.join(reversed(n[int(half):])):
            return True
    else:
        if n[0:int(half+1)] == ''.join(reversed(n[int(half):])):
            return True

    return False


all_condition = False

while all_condition is False:
    if check_palindrome(str(N)) and check_prime_num(int(N))  :
        all_condition = True
    else:
        N += 1

print(N)

