from collections import deque
import sys
#18352번  특정 거리 도시 찾기
# 입력수가 많을 수도 있으므로 sys.stdin사용
# 큐의 pop은 O(n) 따라서 O(1)인 popleft를 사용해야 함

N , M , K , X = map(int, input().split())
load_list = [[] for _ in range(N+1)]

for _ in range(M):
    start , end  = map(int,sys.stdin.readline().split())
    load_list[start].append(end)

#로직
#찐찐막 마지막 테스트 제발

q = deque([X])

#print("거리 정보",load_list)
distance = [-1] * (N+1)
distance[X] = 0

result = 0

while q:
    city = q.popleft()
    for end in load_list[city]:
        if distance[end] == -1 :
            distance[end] = distance[city] +1
            q.append(end)

for idx, d in enumerate(distance):
    if K == d:
        print(idx)
        result += 1

if result == 0:
    print(-1)






