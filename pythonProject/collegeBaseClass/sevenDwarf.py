from itertools import combinations

# 2309번 일곱 난쟁이

dwarf = list()

for i in range(9):
    dwarf.append(int(input()))

dwarf_comb = combinations(dwarf,7)

ans = []
for sum100 in dwarf_comb:
    if sum(sum100) == 100:
        ans = list(sum100)
        break
    else:
        continue

ans.sort()

for i in ans:
    print(i)