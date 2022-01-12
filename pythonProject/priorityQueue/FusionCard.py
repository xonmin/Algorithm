import sys


def solution(deck, m):
    for i in range(m):
        deck.sort()
        deck[0], deck[1] = deck[0] + deck[1], deck[0] + deck[1]

    return sum(deck)


n, m = map(int, sys.stdin.readline().split())
deck = list(map(int, sys.stdin.readline().split()))

print(solution(deck, m))
