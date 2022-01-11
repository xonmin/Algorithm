import sys
import heapq


def solution(n, classTime):
    classTime.sort(key=lambda x: x[0])

    q = []
    heapq.heappush(q, classTime[0][1])

    for i in range(1, n):
        if q[0] > classTime[i][0]:
            heapq.heappush(q, classTime[i][1])
        else:
            heapq.heappop(q)
            heapq.heappush(q, classTime[i][1])

    return len(q)


n = int(sys.stdin.readline())

classTime = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(solution(n, classTime))
