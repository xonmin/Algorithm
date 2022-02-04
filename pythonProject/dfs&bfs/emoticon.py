import sys
from collections import deque

s = int(sys.stdin.readline())


def bfs(s):
    q = deque()
    q.append([1, 0])
    visited = [[-1] * (s + 1) for _ in range(s + 1)]
    visited[1][0] = 0
    while q:
        screen, clip = q.popleft()
        if visited[screen][screen] == -1:  # 1번
            visited[screen][screen] = visited[screen][clip] + 1
            q.append([screen, screen])
        if screen + clip <= s and visited[screen+clip][clip] == -1:
            visited[screen + clip][clip] = visited[screen][clip] + 1
            q.append([screen + clip, clip])
        if screen > 0 and visited[screen-1][clip] == -1:
            visited[screen-1][clip] = visited[screen][clip] + 1
            q.append([screen-1,clip])

    answer = 9999999
    for case in visited[s]:
        if case != -1:
            answer = min(answer,case)
    return answer


print(bfs(s))