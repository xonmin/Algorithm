# n 이하의 소수의 합을 더하는 문제
# 혹은 소수의 개수를 구하는 문제
# 혹은 소수 리스트를 구하는 문제
import math


def isPrime(n):
    # 시간 복잡도 O(n^1/2)

    if n <= 1:
        return False

    if n == 2:
        return False

    for i in range(3, math.sqrt(n)):
        if n % i == 0:
            return False

    return True


def eratostenes(n):
    # 다수의 소수를 찾아야할 때 효과적
    # 어떤 소수 p 에 대해 N 보다 작은 p의 배수 개수 만큼 시간이 걸림
    # 시간 복잡도 O(N log(log(N))
    count = 0  # 소수 개수 구하기
    all_num = [i for i in range(n + 1)]
    all_num[1] = 0 # 1도 소수가 아니니까
    for i in range(2, n + 1):
        if all_num[i] == 0:
            continue
        for j in range(i * 2, n + 1, i):
            all_num[j] = 0

    ans = [i for i in all_num if i != 0]

    return ans


print(eratostenes(59))

