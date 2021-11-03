# Q11724

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n + 1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n + 1)

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1


ans = 0

for i in range(1,n+1):
    if visited[i] == 0:
        bfs(i)
        ans +=1

print(ans)