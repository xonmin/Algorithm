import sys


def solution():
    n = sys.stdin.readline().strip()
    rope = [map(int, sys.stdin.readline().strip()) for r in range(n)]

    # k 개 로프로 w 물체 들어올림
    # 이 때 각 로프에는 w/k 중량 부하
    # 모든 n 개의 로프 사용할 필요 없음
    # 들 수 있는 최대 중량

    rope.sort()
    answer = 0
    for i in range(n):
        w = rope[i]
        answer = max(answer, w * n - i)

    return answer