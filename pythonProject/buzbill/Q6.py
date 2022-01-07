import math
from collections import deque


def connectedSum(graph_nodes, graph_from, graph_to):
    graph = [[] for i in range(graph_nodes + 1)]
    visited = [0] * (graph_nodes + 1)

    for i, j in zip(graph_from, graph_to):
        graph[i].append(j)
        graph[j].append(i)

    ans = []

    def bfs(v):
        q = deque([v])
        count = 1
        visited[v] = 1
        while q:
            v = q.popleft()
            for i in graph[v]:
                if visited[i] == 0:
                    q.append(i)
                    count += 1
                    visited[i] = 1

        return count

    for i in range(1, graph_nodes + 1):
        if visited[i] == 0:
            count = bfs(i)
            ans.append(count)
    print(ans)

    ans = [math.ceil(math.sqrt(a)) for a in ans]
    print(ans)
    return sum(ans)


print(connectedSum(8, [8, 5, 7, 8], [1, 8, 3, 6]))
print(connectedSum(10, [1, 1, 2, 3, 7], [2, 3, 4, 5, 8]))
