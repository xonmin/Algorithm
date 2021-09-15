from collections import deque
N , M , K , X = map(int, input().split())
load_list = [list(map(int,input().split())) for _ in range(M)]

#로직

q = deque()
visited = [False] * (N+1)
satisfied_city = [] # 조건을 만족하는 도시

#print("거리 정보",load_list)
q.append((X,0))
visited[X] = True
count = 0
reach = 0
while q:
    city, count = q.popleft()
    if count == K:
        satisfied_city.append(city)
        continue
    elif count < K:
        for start, end in load_list:
            if start == city and not visited[end] :
                visited[end] = True
                q.append((end, count +1))

if len(satisfied_city) == 0:
    print(-1)
else:
    satisfied_city.sort()
    for city in satisfied_city:
            print(city)





