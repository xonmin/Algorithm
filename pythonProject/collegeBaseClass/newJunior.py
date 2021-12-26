import sys


def solution(t):
    ans = list()
    for i in range(t):
        n = int(sys.stdin.readline())
        junior = list()

        for j in range(n):
            junior.append(list(map(int, sys.stdin.readline().split())))
        count = 1

        junior.sort()

        mini = junior[0][1]
        for j in range(1, n):
            if junior[j][1] < mini:
                mini = junior[j][1]
                count += 1

        ans.append(count)

    for i in ans:
        print(i)


t = int(sys.stdin.readline())

solution(t)
