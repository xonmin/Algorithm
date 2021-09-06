from itertools import combinations
from math import factorial
N , M  = map(int,input().split())

input_str = input()



for i in range(N):
    num_list = list(map(int,input_str.split()))

black_jack = list(combinations(num_list,3))

sum_list = []
for i in range(len(black_jack)):
    sum_list.append(sum(black_jack[i]))

max_value =0
for i in sum_list:
    if i > M :
        continue
    if i < max_value:
        continue
    max_value = i

print(max_value)