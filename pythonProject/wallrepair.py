from itertools import permutations

# 경우의 수 모두 따지기
# len(weak) 만큼의 원소 탐색

def solution(n,weak,dist):
# 외벽 길이 n,
# 취약 지점 위치 배열 week,
# 1시간 동안 이동할 수 있는 거리가 담긴 배열 dist
# 취약 지점을 점검하기 위해 보내야 하는 친구의 최솟값

    # 시계 방향 / 반 시계방향 해결
    # 길이를 두 배로 늘려 고민 해결
    weak_len = len(weak)
    for i in range(weak_len):
        weak.append(weak[i] + n)

    # 투입할 수 잇는 친구의 최댓 값 과 점검 불가능한 경우도 출력 해야하기 때문에 len(dist)+1
    ans = len(dist) + 1
    for i in range(weak_len):
        # 시작 포인트
        start = [weak[j] for j in range (i, i+weak_len)]

        # 벽 점검에 투입할 친구들의 순서
        man_power = permutations(dist,len(dist))

        for order in man_power:
            man_idx , man_count = 0, 1
            # 확인할 수 있는 최대 거리
            check_length = start[0] + order[man_idx]

            for idx in range(weak_len):
                # 한 명이 확인할 수 있는 최대 거리가 넘어가는 경우
                if start[idx] > check_length:
                    # 한 명 더 투입
                    man_count +=1
                    if man_count > len(order):
                        break
                    man_idx +=1
                    check_length = order[man_idx]+ start[idx]
            ans = min(ans,man_count)

    if ans > len(dist):
        return -1

    return ans








n = 12
weak = [1,5,6,10]
dist = [1,2,3,4]
answer = solution(n,weak,dist)
print(answer)

