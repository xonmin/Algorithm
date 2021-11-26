import sys
from collections import deque

t = int(sys.stdin.readline())

'''
9205번 맥주 마시면서 걸어가기 
상근이 집 - 편의점 개수 (N) - 페스티벌 
50m 당 맥주 1개
한 박스에는 20개 
-> 천미터 가기전에 편의점 안나오면 망함 

'''


def case():
    q = deque([start])
    visited = set()
    while q:
        x, y = q.popleft()
        if abs(x - dest[0]) + abs(y - dest[1]) <= 1000:
            return True
        for i in range(n):
            if i not in visited:
                nx, ny = store[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    q.append([nx, ny])
                    visited.add(i)
    return False


for i in range(t):
    n = int(sys.stdin.readline())

    start = list(map(int, sys.stdin.readline().split()))
    store = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dest = list(map(int, sys.stdin.readline().split()))

    if case():
        print("happy")
    else:
        print("sad")
