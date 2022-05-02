import sys

sys.setrecursionlimit(10 ** 9)

n, m = map(int, sys.stdin.readline().split())

parent = [i for i in range(n + 1)]

# union - 서로 다른 트리(집합)을 합ㅊ는 연산 : 더 작은 루트 노드를 기준으로 합친다.

# find - 특정 노드를 인자로 넘겼을 때, 루트 노드를 반환하는 연산 : 루트 노드가 연결되었나 확인 및
# 재귀호출의 형태로 구현 -> 시간복잡도 효율을 높이기 위해 경로 압축 최적화 진행

def find(target):
    if target == parent[target]:  # 본인이 루트 노드면 본인 반환
        return target
    # 경로 압축 최적화
    parent[target] = find(parent[target])  # 루트가 아니라면 재귀를 통해 루트노드찾기
    return parent[target]


def union(a, b):
    a = find(a)
    b = find(b)

    # 작은 루트 노드 기준으로 병합
    if a < b:
        parent[b] = a  # b 원소의 부모는 a
    else:
        parent[a] = b


input_list = list(map(int, sys.stdin.readline().split()) for _ in range(m))
for ip in input_list:
    a, b, c = ip
    if a == 0:
        union(b, c)
    else:
        if find(b) == find(c):
            print('YES')
        else:
            print('NO')
