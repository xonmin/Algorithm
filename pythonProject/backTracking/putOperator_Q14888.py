import sys
from collections import defaultdict
from itertools import permutations

n = int(sys.stdin.readline())

number = list(map(int, sys.stdin.readline().split()))
op_count = list(map(int, sys.stdin.readline().split()))
operator_list = ['+', '-', '*', '//']
op = []

for idx, i in enumerate(op_count):
    for n in range(i):
        op.append(operator_list[n])

oper_per = list(set(permutations(op, len(op))))

answer = []
for i in oper_per:
    k = number[0]
    for j in range(len(number)-1):
        if i[j] == '+':
            k += number[j+1]
        elif i[j] == '-':
            k -= number[j+1]
        elif i[j] == '*':
            k *= number[j+1]
        else:
            if k // number[j+1] < 0:
                k = -(-k//number[j+1])
            else:
                k = k//number[j+1]
    answer.append(k)

print(max(answer))
print(min(answer))