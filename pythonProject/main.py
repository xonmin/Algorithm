import datetime

def solution(lines):
    # 처리 시간은 시작시간과 끝 시간을 모두 포함한다.
    # 끝시간에서 생각했을 때 999 밀리초 이내에 같은 작업이 끝남과 동시에 시작이라면 초당
    # 처리시간은 증가

    traffic = []

    def transTime(time, rangeTime):
        h = int(time[:2]) * 3600
        m = int(time[3:5]) * 60
        s = int(time[6:8])
        milli = int(time[9:])

        endTime = (h + m + s) * 1000 + milli

        duration = int(float(rangeTime[:-1]) * 1000)
        # 문제 조건에 맞춰서 시작시간 1더하기
        startTime = endTime - duration + 1

        return [startTime, endTime]

    for log in lines:
        time = log.split(" ")
        traffic.append(transTime(time[1], time[2]))

    max_ans = 0

    for i in range(len(lines)):
        now_traffic = 0
        cur_endTime = traffic[i][1]
        for j in range(i, len(lines)):
            if cur_endTime > traffic[j][0] - 1000:
                now_traffic += 1

        max_ans = max(now_traffic, max_ans)

    print(max_ans)
    return max_ans


solution([
    "2016-09-15 01:00:04.001 2.0s",
    "2016-09-15 01:00:07.000 2s"
])

solution([
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
])

solution(["2016-09-15 20:59:57.421 0.351s",
          "2016-09-15 20:59:58.233 1.181s",
          "2016-09-15 20:59:58.299 0.8s",
          "2016-09-15 20:59:58.688 1.041s",
          "2016-09-15 20:59:59.591 1.412s",
          "2016-09-15 21:00:00.464 1.466s",
          "2016-09-15 21:00:00.741 1.581s",
          "2016-09-15 21:00:00.748 2.31s",
          "2016-09-15 21:00:00.966 0.381s",
          "2016-09-15 21:00:02.066 2.62s"])

solution([
    "2016-09-15 01:00:04.001 2.0s",
    "2016-09-15 01:00:07.000 2s"
])

solution([
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
])

solution(["2016-09-15 20:59:57.421 0.351s",
          "2016-09-15 20:59:58.233 1.181s",
          "2016-09-15 20:59:58.299 0.8s",
          "2016-09-15 20:59:58.688 1.041s",
          "2016-09-15 20:59:59.591 1.412s",
          "2016-09-15 21:00:00.464 1.466s",
          "2016-09-15 21:00:00.741 1.581s",
          "2016-09-15 21:00:00.748 2.31s",
          "2016-09-15 21:00:00.966 0.381s",
          "2016-09-15 21:00:02.066 2.62s"])


