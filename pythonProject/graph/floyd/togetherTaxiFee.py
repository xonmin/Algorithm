INF = int(1e9)
graph = []


def floyd(n, fares):
    global graph
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for a in range(1, n + 1):
        graph[a][a] = 0

    for info in fares:
        a, b, f = info
        graph[a][b] = f
        graph[b][a] = f

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    return graph


def solution(n, s, a, b, fares):
    fee_table = floyd(n, fares)
    # s-> i  +  i -> a  + i -> b 의 최소 값
    return min([fee_table[i][s] + fee_table[i][a] + fee_table[i][b] for i in range(n+1)])

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
