
from collections import deque
N = int(input())
connect_num = int(input())
connect_line = [[] for _ in range(N+1)]


for i in range(connect_num):
    start, end = (list(map(int,input().split())))
    connect_line[start].append(end)
    connect_line[end].append(start)
visited = [False] * (N+1)

q = deque([1])

result = 0

while q :
    com = q.pop()
    for connect in connect_line[com]:
        if not visited[connect]:
            visited[connect] = True
            q.append(connect)



visited[1] = False;

count = 0
for idx in visited:
    if idx:
        count += 1


print(count)
