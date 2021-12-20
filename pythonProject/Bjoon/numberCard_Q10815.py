import sys

n = int(sys.stdin.readline())

card = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

compare = list(map(int, sys.stdin.readline().split()))

ans = []

card.sort()

# 이진 탐색
for i in compare:
    first = 0
    end = n - 1
    while first <= end:
        middle = (first + end) // 2
        if i == card[middle]:
            ans.append(1)
            break
        elif i > card[middle]:
            first = middle + 1
        else:
            end = middle - 1
    else:
        ans.append(0)

for i in ans:
    print(i, end=" ")
