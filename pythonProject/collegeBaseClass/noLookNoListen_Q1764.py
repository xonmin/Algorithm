# 백준 1764번 듣보잡
import sys

n, m = map(int,sys.stdin.readline().split())

noLook_set = set()
noListen_set = set()

for i in range(n):
    noLook_set.add(sys.stdin.readline().rstrip())
for i in range(m):
    noListen_set.add(sys.stdin.readline().rstrip())

noLookNoListen_set = list(noLook_set & noListen_set)
noLookNoListen_set.sort()

print(len(noLookNoListen_set))
for _ in noLookNoListen_set:
    print(_)