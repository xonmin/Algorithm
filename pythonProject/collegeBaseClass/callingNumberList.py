import sys

t = int(sys.stdin.readline())


def chk(numlist):
    numlist.sort()
    for p1, p2 in zip(numlist, numlist[1:]):
        if p2.startswith(p1):
            return False
    return True


answer = list()
for i in range(t):
    n = int(sys.stdin.readline())
    numberList = [sys.stdin.readline().rstrip() for _ in range(n)]
    if chk(numberList):
        answer.append("YES")
    else:
        answer.append("NO")

for _ in answer:
    print(_)
