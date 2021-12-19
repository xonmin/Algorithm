import sys

x = int(sys.stdin.readline())

'''
숫자 1, 2, 3으로만 이루어지는 수열이 있다.
임의의 길이의 인접한 두 개의 부분 수열이 동일한 것이 있으면,
그 수열을 나쁜 수열이라고 부른다. 그렇지 않은 수열은 좋은 수열이다.
'''


def solve(x):
    ans = []

    def backTrack(idx):
        for i in range(1, (idx // 2) + 1):
            if ans[-i:] == ans[-2 * i:-i]:
                return -1

        if idx == x:
            for i in range(x):
                print(ans[i], end='')
            return 0

        for i in range(1, 4):
            ans.append(i)
            if backTrack(idx + 1) == 0:
                return 0
            ans.pop()

    backTrack(0)


solve(x)
