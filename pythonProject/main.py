# 백준 15686 문제 nxn 도시
# 0 - 빈 칸 1 - 집 2 - 치킨 집
# 거리 계산  |r1 - r2|  + |c1 - c2|
# 기존 다른 팀원들 풀었던 문제
from itertools import combinations

N , M = map(int, input().split())
# 이차원 배열 입력 받기
city = [list(map(int,input().split())) for _ in range(N)]

# M 개만 남기고 나머지 0으로 만든 경우의 수
# 치킨 집의 위치 인덱스를 담을 튜플 리스트
chicken_location = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken_location.append((i,j))

# 치킨 집 M 개 남는 경우의 수
survive_chicken = list(combinations(chicken_location,M))


# 도시 전체 치킨 거리가 최소가 될 때 찾기
best_location = 999999999
for chicken_list in survive_chicken:

    # 집들을 기준으로 최소의 경우 찾기
    temp_ans = 0
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                # 그 집에서 가장 가까운 치킨 집과 거리 계산
                base_home = 999999

                for each_chicken in chicken_list:
                    base_home = min(base_home , abs(i - each_chicken[0]) + abs(j - each_chicken[1]))
                temp_ans += base_home

    best_location = min(temp_ans,best_location)

print(best_location)