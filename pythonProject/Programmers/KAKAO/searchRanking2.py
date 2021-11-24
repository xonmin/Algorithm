def solution(info, query):

    result = []

    for q in range(len(query)):
        queryList = query[q].replace('and ', '').split(' ')
        q_point = int(queryList.pop())

        count = 0

        for i in range(len(info)):
            infoList = info[i].split(' ')
            i_point = int(infoList.pop())
            ignoreCount = queryList.count('-')
            resultSet = set(queryList) & set(infoList)

            if q_point <= i_point and (len(resultSet) + ignoreCount) == 4  :
                count += 1

        result.append(count)

    answer = result
    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
          "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
          "- and - and - and - 150"]))