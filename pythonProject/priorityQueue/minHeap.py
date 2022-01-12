import heapq
import sys

def solution(arr):
    q = []
    ans = []
    for num in arr:
        if num == 0:
            if not q:
                ans.append(0)
            else:
                ans.append(heapq.heappop(q))
        else:
            heapq.heappush(q,num)
            ans.append(heapq.heappop(q))

    for _ in ans:
        print(_)


n = int(sys.stdin.readline())

arr = [int(sys.stdin.readline()) for _ in range(n)]

solution(arr)