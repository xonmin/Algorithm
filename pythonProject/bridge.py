from math import factorial

T = int(input())

for i in range(T):
    N, M  = input().split()
    N , M  = int(N), int(M)
    ans = factorial(M) // (factorial(N) * factorial(M-N))

    print(ans)