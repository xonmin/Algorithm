def solution(time, plans):

    destination = []
    start_time = []
    arrive_time = []
    trip_list = []

    trip_list.append('호치민')
    for plan in plans:

        destination.append(plan[0])
        if "PM" in plan[1]:
            idx = plan[1].find('PM')
            start_time.append(int(plan[1][:idx]) + 12)
        else:
            idx = plan[1].find('AM')
            start_time.append(int(plan[1][:idx]))

        if "PM" in plan[2]:
            idx = plan[2].find('PM')
            arrive_time.append(int(plan[2][:idx]) + 12)
        else:
            idx = plan[2].find('AM')
            arrive_time.append(int(plan[2][:idx]))

    for i in range(len(destination)):

        need_start_time = float(start_time[i]) - 21.5
        need_arrive_time = float(arrive_time[i]) - 13

        if need_start_time > 0:
            need_start_time = 0

        if need_arrive_time < 0:
            need_arrive_time = 0

        if abs(need_start_time) + abs(need_arrive_time) <= time:
            trip_list.pop()
            trip_list.append(destination[i])

    answer = "".join(trip_list[-1])

    return answer


