

def solution(n, t, m, timetable):
    '''
    9시부터 n 회 t 분 간격으로 역에 도착
    하나의 셔틀에 m 명 승객 탑승
    모든 크루는 23:59에 집에 들어간다.
    '''

    # 분으로 초기화
    timetable = [int(t[:2]) * 60 + int(t[3:5]) for t in timetable]
    timetable.sort()
    last = 540 + (n - 1) * t  # 마지막 버스

    for i in range(n):
        if len(timetable) < m:  # 대기 인원이 다 탈 수 있다면
            return str(last // 60).zfill(2) + ':' + str(last % 60).zfill(2)
        if i == n - 1:  # 마지막 차
            if timetable[0] <= last:  # 마지막 놈보다 빨리 타기
                last = timetable[m - 1] - 1
            return str(last // 60).zfill(2) + ':' + str(last % 60).zfill(2)

        for j in range(m - 1, -1, -1):
            # del 을 통해 제거할 경우 인덱스 변화에 영향 주지 않기 위해 거꾸로
            next_bus = (60 * 9) + i * t
            if timetable[j] <= next_bus:  # 앞서 타는 놈들 없애기
                del timetable[j]


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
