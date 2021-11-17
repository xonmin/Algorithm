def solution(N, stages):
    answer = []

    user_num = len(stages)

    success = [0] * (N + 2)
    nice_try = [0] * (N + 2)

    for i in range(0, user_num):
        #print(stages[i] - 1)
        success[stages[i]-1] += 1
        for j in range(stages[i]):
            nice_try[j] += 1

    fail = list()
    #print(success)
    #print(nice_try)
    for i in range(N):
        #print(i)
        if nice_try[i] == 0:
            fail.append([0, i])
        else:
            fail.append([success[i] / nice_try[i], i])

    fail.sort(key=lambda x: (x[0]) , reverse=True)

    for i in range(N):
        answer.append(fail[i][1] + 1)

    #print(fail)
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
