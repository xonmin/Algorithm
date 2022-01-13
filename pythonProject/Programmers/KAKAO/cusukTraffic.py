import datetime


def solution(lines):
    answer = 0

    traffic = []

    def transTime(lines):

        line_split = lines.split()
        timeSplit = line_split[1].split(":")

        seconds = float(timeSplit[0]) * 3600 + float(timeSplit[1]) * 60 + float(timeSplit[2])
        rangeTime = float(line_split[2][0:-1])

        startTime = seconds - rangeTime + 0.001
        endTime = seconds + 1

        return [startTime, endTime]

    for log in lines:
        traffic.append(transTime(log))

    traffic.sort()

    max_ans = 0
    print(traffic)
    for idx, log in enumerate(traffic):
        now_traffic = 1
        for comp in traffic[idx + 1:]:
            if comp[0] < log[1]:
                now_traffic += 1
                max_ans = max(now_traffic, max_ans)
            else:
                break

    if max_ans == 0:
        return 1
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
