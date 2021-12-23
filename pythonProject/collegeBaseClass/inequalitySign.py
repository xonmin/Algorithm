import sys
from itertools import permutations
from string import digits


def solution():
    def chk(p, inEqual):
        for i in range(len(inEqual)):
            if inEqual[i] == '<':
                if int(p[i]) > int(p[i + 1]):
                    return False
            else:
                if int(p[i]) < int(p[i + 1]):
                    return False
        return True

    def exe():
        k = int(sys.stdin.readline())
        inEqual = sys.stdin.readline().split()

        num_list = list(digits.strip())

        per = permutations(num_list, k + 1)

        maxi = "0"
        mini = "999999999999999"
        for p in per:

            if chk(p, inEqual):
                maxi = max("".join(p), maxi)
                mini = min("".join(p), mini)

        if len(maxi) == k:
            maxi = "0" + maxi
        if len(mini) == k:
            mini = "0" + mini

        return maxi, mini

    ans1, ans2 = exe()
    print(ans1)
    print(ans2)


solution()
