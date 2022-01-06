import sys
from collections import deque


def solution(n, m, v):
    graph = [[False] * (n + 1) for i in range(n + 1)]

    for i in range(m):
        u, k = map(int, sys.stdin.readline().split())
        graph[u][k] = True
        graph[k][u] = True

    visited = [False] * (n + 1)

    def DFS(x): # 갈 수 있는 최대 방문할 수 있는 길이
        #경로에 따른 특징이 필요할 떄
        # 검색 대상의 그래프가 너무 클 때
        # count #O(n^2) #모든
        ans = [x]
        visited[x] = True
        for i in range(1, n + 1):
            if graph[x][i] is True and visited[i] is False:
                ans += DFS(i)

        return ans

    def BFS(x): #미로 찾기 ,  최단경로 찾을 떄 , 인접 행렬  O(n^2)
        # 인접 리스트 O(n + e)
        ans = []
        q = deque()
        q.append(x)

        visited = [False] * (n + 1)
        visited[x] = True
        ans.append(x)

        while q:
            now_node = q.popleft()
            for i in range(1, n + 1):
                if graph[now_node][i] is True and visited[i] is False:
                    q.append(i)
                    ans.append(i)
                    visited[i] = True
        return ans

    dfs_ans = DFS(v)
    bfs_ans = BFS(v)

    for i in dfs_ans:
        print(i, end=" ")
    print()
    for i in bfs_ans:
        print(i, end=" ")


n, m, v = map(int, sys.stdin.readline().split())

solution(n, m, v)
