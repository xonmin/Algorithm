import bisect, itertools, collections


def solution(info, query):
    answer = []
    infomap = collections.defaultdict(list)
    # true와 false를 통한 4가지 구성 경우의 수
    binarys = list(itertools.product((True, False), repeat=4))

    for inf in info:
        inf = inf.split()
        for binary in binarys:
            key = "".join([inf[i] if binary[i] else '-' for i in range(4)])
            infomap[key].append(int(inf[4]))

    for k in infomap.keys():
        infomap[k].sort()

    for q in query:
        lang, _, position, _, career, _, food, point = q.split()
        key = ''.join([lang, position, career, food])
        i = bisect.bisect_left(infomap[key], int(point))
        answer.append(len(infomap[key]) - i)

    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
     "- and - and - and chicken 100", "- and - and - and - 150"]))
