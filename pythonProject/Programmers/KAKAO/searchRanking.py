def solution(info, query):
    answer = []

    q_list = list()
    info_list = list()

    for i in info:
        info_list.append(i.split())
        info_list[-1][-1] = int(info_list[-1][-1])
    for q in query:
        q = q.replace("and", "")
        q_list.append(q.split())
        q_list[-1][-1] = int(q_list[-1][-1])

    for q in q_list:
        condition_met = 0

        dash_idx = findDash(q)
        chk_idx = [i for i in range(4) if i not in dash_idx]
        temp_info = [t[:-1] for t in info_list if t[-1] >= q[-1]]
        q2 = [q[i] for i in chk_idx]

        for t in temp_info:
            t = [t[i] for i in chk_idx]
            if q2 == t:
                condition_met += 1

        answer.append(condition_met)

    return answer


def findDash(q):
    n = -1
    result = []
    while True:
        if q[n + 1:].count('-') == 0:
            break
        n += q[n + 1:].index('-') + 1
        result.append(n)
    return result


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
