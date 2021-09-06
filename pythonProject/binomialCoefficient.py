from itertools import combinations
from math import factorial

N, K = input().split()

N = int(N)
K = int(K)

ans = factorial(N) // (factorial(K)*factorial(N-K))

print(ans)