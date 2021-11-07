def solution(log):
    answer = ''
    log = list_split(log, 2)
    all_time = 0

    for study in log:

        start, end = study[0], study[1]

        start_time = start.split(":")

        calc_start = int(start_time[0]) * 60 + int(start_time[1])

        end_time = end.split(":")
        calc_end = int(end_time[0]) * 60 + int(end_time[1])

        study_time = calc_end - calc_start

        if study_time < 5:
            study_time = 0
        elif study_time > 105:
            study_time = 105

        all_time += study_time

    hour, minute = 0, 0
    if all_time // 60 < 10:
        hour = '0' + str(all_time // 60)
    else:
        hour = str(all_time // 60)

    if all_time % 60 < 10:
        minute = '0' + str(all_time % 60)
    else:
        minute = str(all_time % 60)

    answer = hour + ':' + minute

    return answer


def list_split(log, n):
    return [log[i:i + n] for i in range(0, len(log), n)]


print(solution(["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]))
