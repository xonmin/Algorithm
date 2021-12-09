from collections import deque

global graph
global nodes


def solution(tree_nodes, tree_from, tree_to):
    global graph, nodes
    graph = [[] for i in range(tree_nodes + 1)]

    nodes = [[0] * (tree_nodes + 1) for _ in range(tree_nodes + 1)]

    for i in range(tree_nodes - 1):
        graph[tree_from[i]].append(tree_to[i])
        graph[tree_to[i]].append(tree_from[i])

    for i in range(1, tree_nodes + 1):
        bfs(i, tree_nodes)

    diameter = max(max(nodes))

    ans = []

    for i in range(1, tree_nodes + 1):

        if nodes[i].count(diameter) == 0:
            ans.append(0)
        else:
            ans.append(1)

    return ans


def bfs(v, tree_nodes):
    q = deque()
    q.append([v, 0])
    visited = [False] * (tree_nodes + 1)
    visited[v] = True
    start = v
    while q:
        v, num = q.popleft()
        for i in graph[v]:
            if visited[i] is False:
                visited[i] = True
                nodes[start][i] = num + 1
                q.append([i, num + 1])

    # print(start, "번쨰 노드 거리 : ", nodes[v])


print(solution(7, [1, 2, 3, 3, 1, 1], [2, 3, 4, 5, 6, 7]))
print(solution(2, [2], [1]))
