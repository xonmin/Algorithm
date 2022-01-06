import sys


def solution(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    result_str = str(result)
    ans = 0
    for i in range(len(result_str) - 1, 0, -1):
        if result_str[i] == '0':
            ans += 1
        else:
            break
    return ans


def effiecient_sol(n):
    # 2의 계승과 5의 계승을 세어 최소값 반환
    # O(nlogn)

    two, five = 0, 0
    for n in range(1, N + 1):
        while n % 2 == 0:
            two += 1
            n //= 2
        while n % 5 == 0:
            five += 1
            n //= 5
    return min(two, five)


n = int(sys.stdin.readline())
print(solution(n))
